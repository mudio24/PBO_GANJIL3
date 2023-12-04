import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

class LimasSegitigaCalculator:
    def __init__(self, master):
        self.master = master
        master.title("KALKULATOR LUAS DAN VOLUME LIMAS SEGITIGA")

        self.frame = Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.nama = Label(self.frame, text="220511121 MUHAMAD DIO ANUGRAHA")
        self.nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.alas_label = Label(self.frame, text="Alas:")
        self.alas_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.tinggi_label = Label(self.frame, text="Tinggi:")
        self.tinggi_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.TL_label = Label(self.frame, text="Tinggi Limas:")
        self.TL_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.txtalas = Entry(self.frame)
        self.txtalas.grid(row=1, column=1)

        self.txttinggi = Entry(self.frame)
        self.txttinggi.grid(row=2, column=1)

        self.txtTL = Entry(self.frame)
        self.txtTL.grid(row=3, column=1)

        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        self.luas_label = Label(self.frame, text="Luas :")
        self.luas_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.volume_label = Label(self.frame, text="Volume :")
        self.volume_label.grid(row=6, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(self.frame)
        self.txtLuas.grid(row=5, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(self.frame)
        self.txtVolume.grid(row=6, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        alas = float(self.txtalas.get())
        tinggi = float(self.txttinggi.get())
        TL = float(self.txtTL.get())
        L = round(((1/2 * alas * tinggi) + (1/2 * alas * tinggi) + (1/2 * alas * tinggi) + (1/2 * alas * tinggi)), 2)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        alas = float(self.txtalas.get())
        tinggi = float(self.txttinggi.get())
        TL = float(self.txtTL.get())
        V = round((1/6 * alas * tinggi * TL), 2)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()


if __name__ == "__main__":
    root = tk.Tk()
    app = LimasSegitigaCalculator(root)
    root.mainloop()
