import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W
from math import pi

class TabungCalculator:
    def __init__(self, master):
        self.master = master
        master.title("KALKULATOR LUAS DAN VOLUME TABUNG")

        self.frame = Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.nama = Label(self.frame, text="220511121 MUHAMAD DIO ANUGRAHA")
        self.nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.jari_jari_label = Label(self.frame, text="Jari-jari:")
        self.jari_jari_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.tinggi_label = Label(self.frame, text="Tinggi Tabung:")
        self.tinggi_label.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.txtjari_jari = Entry(self.frame)
        self.txtjari_jari.grid(row=1, column=1)

        self.txttinggi = Entry(self.frame)
        self.txttinggi.grid(row=2, column=1)

        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        self.luas_label = Label(self.frame, text="Luas :")
        self.luas_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.volume_label = Label(self.frame, text="Volume :")
        self.volume_label.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(self.frame)
        self.txtLuas.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(self.frame)
        self.txtVolume.grid(row=5, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        r = float(self.txtjari_jari.get())
        tinggi = float(self.txttinggi.get())
        L = round(((2*pi*r*tinggi) + (2*pi*r**2)), 2)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        r = float(self.txtjari_jari.get())
        tinggi = float(self.txttinggi.get())
        V = round((pi * r**2 * tinggi), 2)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()


if __name__ == "__main__":
    root = tk.Tk()
    app = TabungCalculator(root)
    root.mainloop()
