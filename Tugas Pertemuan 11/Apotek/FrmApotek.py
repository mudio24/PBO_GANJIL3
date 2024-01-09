import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, StringVar, messagebox
from Obat import Obat  # Anda mungkin perlu membuat kelas Obat sendiri

class FormObat:
    
    def __init__(self, parent, title): 
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='Kode Obat:').grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtKodeObat = Entry(mainFrame) 
        self.txtKodeObat.grid(row=0, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Nama Obat:').grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtNamaObat = Entry(mainFrame) 
        self.txtNamaObat.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Berat:').grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtBerat = Entry(mainFrame) 
        self.txtBerat.grid(row=2, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Bentuk:').grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.txtBentuk = StringVar()
        bentuk_obat = ['Tablet', 'Kapsul', 'Kaplet', 'Pil', 'Serbuk', 'Obat Oles', 'Obat Cair', 'Obat Tetes']
        for index, bentuk in enumerate(bentuk_obat):
            Radiobutton(mainFrame, text=bentuk, value=bentuk, variable=self.txtBentuk).grid(row=3+index, column=1, padx=5, pady=2, sticky=tk.W)

        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        self.btncari = Button(mainFrame, text='cari', command=self.onCari, width=10)
        self.btncari.grid(row=3+len(bentuk_obat), column=3, padx=5, pady=5)

        # Treeview
        columns = ('kode_obat', 'nama_obat', 'berat', 'bentuk')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=80)
        self.tree.grid(row=6+len(bentuk_obat), column=0, columnspan=4, padx=5, pady=5, sticky=tk.W+tk.E)

  
    def onClear(self, event=None):
        self.txtKodeObat.delete(0, END)
        self.txtNamaObat.delete(0, END)
        self.txtBerat.delete(0, END)
        self.txtBentuk.set("")

    def onReload(self, event=None):
        obat = Obat()
        result = obat.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row_data in result:
            self.tree.insert('', END, values=row_data)

    def onKeluar(self):
        self.parent.destroy()

    def onSimpan(self):
        # Ambil data dari inputan
        kode_obat = self.txtKodeObat.get()
        nama_obat = self.txtNamaObat.get()
        berat = self.txtBerat.get()
        bentuk = self.txtBentuk.get()

        # Validasi inputan (misalnya, pastikan semua kolom diisi)
        if not all([kode_obat, nama_obat, berat, bentuk]):
            messagebox.showwarning("Peringatan", "Semua kolom harus diisi!")
            return

        # Simpan data obat ke database atau tempat penyimpanan lainnya
        obat_baru = Obat()
        obat_baru.kode_obat = kode_obat
        obat_baru.nama_obat = nama_obat
        obat_baru.berat = berat
        obat_baru.bentuk = bentuk

        result = obat_baru.simpan()  # Anda perlu mengimplementasikan metode simpan di kelas Obat Anda

        if result:
            messagebox.showinfo("Informasi", "Data obat berhasil disimpan!")
            self.onReload()  # Muat ulang data di Treeview
        else:
            messagebox.showerror("Error", "Gagal menyimpan data obat!")

    def onDelete(self):
        # Ambil kode obat dari inputan
        kode_obat = self.txtKodeObat.get()

        # Validasi kode obat (pastikan kode obat diisi)
        if not kode_obat:
            messagebox.showwarning("Peringatan", "Kode Obat harus diisi!")
            return

        # Lakukan konfirmasi penghapusan data
        confirm = messagebox.askyesno("Konfirmasi", f"Apakah Anda yakin ingin menghapus obat dengan kode {kode_obat}?")

        if confirm:
            # Hapus data obat dari database atau tempat penyimpanan lainnya
            obat = Obat()
            obat.kode_obat = kode_obat

            # Anda perlu mengimplementasikan metode delete dengan kode_obat di kelas Obat Anda
            result = obat.delete()  

            if result:
                messagebox.showinfo("Informasi", "Data obat berhasil dihapus!")
                self.onReload()  # Muat ulang data di Treeview
            else:
                messagebox.showerror("Error", "Gagal menghapus data obat!")

                
    def onCari(self):
        # Ambil teks dari inputan pencarian
        teks_pencarian = self.txtKodeObat.get()

        # Validasi teks pencarian (pastikan teks pencarian diisi)
        if not teks_pencarian:
            messagebox.showwarning("Peringatan", "Kode Obat atau Nama Obat harus diisi untuk pencarian!")
            return

        # Lakukan pencarian data obat di database atau tempat penyimpanan lainnya
        obat = Obat()
        result = obat.cari(teks_pencarian)

        # Perbarui Treeview dengan hasil pencarian
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row_data in result:
            self.tree.insert('', END, values=row_data)



    
    # Tambahkan method onCari(), TampilkanData(), onSimpan(), onDelete(), dan onKeluar() sesuai kebutuhan Anda.

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("700x300")
    aplikasi = FormObat(root, "Aplikasi Data Obat")
    root.mainloop()
