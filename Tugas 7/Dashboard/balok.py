import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

class BalokCalculator:
    def __init__(self, master):
        self.master = master
        master.geometry('380x410')
        master.title("Program Menghitung volume dan luas permukaan Balok")

        self.frame = Frame(master)
        self.frame.pack(padx=30, pady=30)

        self.label_nim = Label(self.frame, text='220511121')
        self.label_nim.grid(row=8, column=0, sticky=W, padx=5, pady=5)

        self.label_nama = Label(self.frame, text='MUHAMAD DIO ANUGRAHA')
        self.label_nama.grid(row=9, column=0, sticky=W, padx=5, pady=5)

        self.label_balok = Label(self.frame, text='Balok: ')
        self.label_balok.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.label_panjang = Label(self.frame, text='Panjang: ')
        self.label_panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.label_lebar = Label(self.frame, text='Lebar: ')
        self.label_lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.label_tinggi = Label(self.frame, text='Tinggi: ')
        self.label_tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.label_volume = Label(self.frame, text='Volume: ')
        self.label_volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

        self.label_luas_permukaan = Label(self.frame, text='Luas Permukaan: ')
        self.label_luas_permukaan.grid(row=7, column=0, sticky=W, padx=8, pady=8)

        self.hitung_volume_button = Button(self.frame, text="Hitung Volume", command=self.hitung_volume)
        self.hitung_volume_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

        self.hitung_luas_permukaan_button = Button(self.frame, text="Hitung Luas Permukaan", command=self.hitung_luas_permukaan)
        self.hitung_luas_permukaan_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

        self.txt_panjang = Entry(self.frame)
        self.txt_panjang.grid(row=1, column=1)

        self.txt_lebar = Entry(self.frame)
        self.txt_lebar.grid(row=2, column=1)

        self.txt_tinggi = Entry(self.frame)
        self.txt_tinggi.grid(row=3, column=1)

        self.txt_volume = Entry(self.frame)
        self.txt_volume.grid(row=5, column=1)

        self.txt_luas_permukaan = Entry(self.frame)
        self.txt_luas_permukaan.grid(row=7, column=1)

    def hitung_volume(self):
        panjang = float(self.txt_panjang.get())
        lebar = float(self.txt_lebar.get())
        tinggi = float(self.txt_tinggi.get())

        V = round(panjang * lebar * tinggi, 2)

        self.txt_volume.delete(0, END)
        self.txt_volume.insert(END, V)

    def hitung_luas_permukaan(self):
        panjang = float(self.txt_panjang.get())
        lebar = float(self.txt_lebar.get())
        tinggi = float(self.txt_tinggi.get())

        lp = round(2 * (panjang * lebar + panjang * tinggi + lebar * tinggi), 2)

        self.txt_luas_permukaan.delete(0, END)
        self.txt_luas_permukaan.insert(END, lp)


if __name__ == "__main__":
    root = tk.Tk()
    app = BalokCalculator(root)
    root.mainloop()
