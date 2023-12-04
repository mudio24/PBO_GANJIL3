import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

class KubusCalculator:
    def __init__(self, master):
        self.master = master
        master.title("KALKULATOR LUAS DAN VOLUME KUBUS")

        self.frame = Frame(master)
        self.frame.pack(padx=40, pady=40)

        self.nama = Label(self.frame, text="220511121 MUHAMAD DIO ANUGRAHA")
        self.nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.sisi_label = Label(self.frame, text="sisi:")
        self.sisi_label.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        self.txtsisi = Entry(self.frame)
        self.txtsisi.grid(row=1, column=1)

        self.hitung_button = Button(self.frame, text="Hitung", command=self.hitung)
        self.hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

        self.luas_label = Label(self.frame, text="Luas :")
        self.luas_label.grid(row=3, column=0, sticky=W, padx=5, pady=5)

        self.volume_label = Label(self.frame, text="volume :")
        self.volume_label.grid(row=4, column=0, sticky=W, padx=5, pady=5)

        self.txtLuas = Entry(self.frame)
        self.txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

        self.txtVolume = Entry(self.frame)
        self.txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

    def hitung_luas(self):
        s = float(self.txtsisi.get())
        L = round((6 * s**2), 2)
        self.txtLuas.delete(0, END)
        self.txtLuas.insert(END, L)

    def hitung_volume(self):
        s = float(self.txtsisi.get())
        V = round((s**3), 2)
        self.txtVolume.delete(0, END)
        self.txtVolume.insert(END, V)

    def hitung(self):
        self.hitung_luas()
        self.hitung_volume()


if __name__ == "__main__":
    root = tk.Tk()
    app = KubusCalculator(root)
    root.mainloop()
