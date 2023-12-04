from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, ttk
from googletrans import Translator, LANGUAGES

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        background_label = Label(mainFrame, text='', bg='#f8c51d')
        background_label.place(relwidth=1, relheight=1)
        
        Label(mainFrame, text="Pilih Bahasa :", bg="#d5a506").grid(row=0, column=0, pady=5, padx=5)
        # Pasang Combobox untuk pilihan bahasa di paling atas
        self.comboboxBahasa = ttk.Combobox(mainFrame, values=list(LANGUAGES.values()), state="readonly")
        self.comboboxBahasa.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.comboboxBahasa.set('Indonesian')  # Pilihan default
        
        # Pasang Label
        Label(mainFrame, text='Masukkan teks:', bg="#d5a506").grid(row=7, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:', bg="#d5a506").grid(row=9, column=0, sticky=W, padx=5, pady=5)

        # Pasang Textbox
        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=7, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=9, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!', bg="#72dc72", command=self.onTranslate)
        self.btnTranslate.grid(row=8, column=1, padx=5, pady=5) 
        
        #NIM & NAMA
        Label(mainFrame, text="220511121", bg="#fbe18c").grid(row=12, column=1, pady=10, padx=10)
        Label(mainFrame, text="MUHAMAD DIO  ANUGRAHA", bg="#fbe18c").grid(row=13, column=1, pady=10, padx=10)

    def onTranslate(self):
        self.txtHasil.delete('0', END)
        
        penterjemah = Translator()
        bahasa_tujuan = [k for k, v in LANGUAGES.items() if v == self.comboboxBahasa.get()][0]

        hasil = penterjemah.translate(self.txtSumber.get(), src='id', dest=bahasa_tujuan) 
        self.txtHasil.insert(END, hasil.text)
        
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop()
