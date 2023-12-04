import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

class PrismaSegitigaCalculator:
    def __init__(self, master):
        self.master = master
        master.title("KALKULATOR LUAS DAN VOLUME PRISMA SEGITIGA")

        self.frame = Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.nama = Label(self.frame, text="220511121 MUHAMAD DIO ANUGRAHA")
        self.nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.alas_label = Label(self.frame, text="Alas:")
        self.alas_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.tinggi_label = Label(self.frame, text="Tinggi:")
        self.tinggi_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.Tp_label = Label(self.frame, text="Tinggi Prisma:")
        self.Tp_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.sisi1_label = Label(self.frame, text="Sisi 1:")
        self.sisi1_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.sisi2_label = Label(self.frame, text="Sisi 2:")
        self.sisi2_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.sisi3_label = Label(self.frame, text="Sisi 3:")
        self.sisi3_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtalas = Entry(self.frame)
        self.txtalas.grid(row=1, column=1)

        self.txttinggi = Entry(self.frame)
        self.txttinggi.grid(row=2, column=1)

        self.txtTp = Entry(self.frame)
        self.txtTp.grid(row=3, column=1)

        self.txtsisi1 = Entry(self.frame)
        self.txtsisi1.grid(row=4, column=1)

        self.txtsisi2 = Entry(self.frame)
        self.txtsisi2.grid(row=5, column=1)

        self.txtsisi3 = Entry(self.frame)
        self.txtsisi3.grid(row=6, column=1)

        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=7, column=1, sticky=W, padx=5, pady=5)

        self.luas_label = Label(self.frame, text="Luas :")
        self.luas_label.grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.volume_label = Label(self.frame, text="Volume :")
        self.volume_label.grid(row=9, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(self.frame)
        self.txtLuas.grid(row=8, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(self.frame)
        self.txtVolume.grid(row=9, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        alas = float(self.txtalas.get())
        tinggi = float(self.txttinggi.get())
        Tp = float(self.txtTp.get())
        sisi1 = float(self.txtsisi1.get())
        sisi2 = float(self.txtsisi2.get())
        sisi3 = float(self.txtsisi3.get())
        L = round(((2*(1/2*alas*tinggi)) + ((sisi1 + sisi2 + sisi3)*Tp)), 2)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        alas = float(self.txtalas.get())
        tinggi = float(self.txttinggi.get())
        Tp = float(self.txtTp.get())
        sisi1 = float(self.txtsisi1.get())
        sisi2 = float(self.txtsisi2.get())
        sisi3 = float(self.txtsisi3.get())
        V = round(((1/2*alas*tinggi)*Tp), 2)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()


if __name__ == "__main__":
    root = tk.Tk()
    app = PrismaSegitigaCalculator(root)
    root.mainloop()
