import tkinter as tk
from tkinter import Frame, Label, Entry, Button, END, W

def hitung_volume():
    panjang = float(txt_panjang.get())
    lebar = float(txt_lebar.get())
    tinggi = float(txt_tinggi.get())
    
    V = round(panjang * lebar * tinggi, 2)
    
    txt_volume.delete(0, END)
    txt_volume.insert(END, V)

def hitung_luas_permukaan():
    panjang = float(txt_panjang.get())
    lebar = float(txt_lebar.get())
    tinggi = float(txt_tinggi.get())
    
    lp = round(2 * (panjang * lebar + panjang * tinggi + lebar * tinggi), 2)
    
    txt_luas_permukaan.delete(0, END)
    txt_luas_permukaan.insert(END, lp)

def hitung():
    hitung_volume()
    hitung_luas_permukaan()

app = tk.Tk()
app.geometry('380x410')
app.title("Program Menghitung volume dan luas permukaan Balok")

Frame = Frame(app)
Frame.pack(padx=30, pady=30)

nama = Label(Frame, text='220511121')
nama.grid(row=8, column=0, sticky=W, padx=5, pady=5)

nama = Label(Frame, text='MUHAMAD DIO ANUGRAHA')
nama.grid(row=9, column=0, sticky=W, padx=5, pady=5)

nama = Label(Frame, text='Balok: ')
nama.grid(row=0, column=0, sticky=W, padx=5, pady=5)

panjang = Label(Frame, text='Panjang: ')
panjang.grid(row=1, column=0, sticky=W, padx=5, pady=5)

lebar = Label(Frame, text='Lebar: ')
lebar.grid(row=2, column=0, sticky=W, padx=5, pady=5)

tinggi = Label(Frame, text='Tinggi: ')
tinggi.grid(row=3, column=0, sticky=W, padx=5, pady=5)

volume = Label(Frame, text='Volume: ')
volume.grid(row=5, column=0, sticky=W, padx=5, pady=5)

luas_permukaan = Label(Frame, text='Luas Permukaan: ')
luas_permukaan.grid(row=7, column=0, sticky=W, padx=8, pady=8)

hitung_volume_button = Button(Frame, text="Hitung Volume", command=hitung_volume)
hitung_volume_button.grid(row=4, column=1, sticky=W, padx=5, pady=5)

hitung_luas_permukaan_button = Button(Frame, text="Hitung Luas Permukaan", command=hitung_luas_permukaan)
hitung_luas_permukaan_button.grid(row=6, column=1, sticky=W, padx=5, pady=5)

txt_panjang = Entry(Frame)
txt_panjang.grid(row=1, column=1)

txt_lebar = Entry(Frame)
txt_lebar.grid(row=2, column=1)

txt_tinggi = Entry(Frame)
txt_tinggi.grid(row=3, column=1)

txt_volume = Entry(Frame)
txt_volume.grid(row=5, column=1)

txt_luas_permukaan = Entry(Frame)
txt_luas_permukaan.grid(row=7, column=1)


app.mainloop()