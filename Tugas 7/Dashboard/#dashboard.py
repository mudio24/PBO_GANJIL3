import tkinter as tk
from tkinter import Menu

from balok import BalokCalculator
from bola import BolaCalculator
from kubus import KubusCalculator
from limas_segiempat import LimasSegiempatCalculator
from limas_segitiga import LimasSegitigaCalculator
from prisma_segitiga import PrismaSegitigaCalculator
from tabung import TabungCalculator

def destroy_window(window):
    window.destroy()

def new_window(_class):
    new = tk.Toplevel(root)
    new.title(_class.__name__)
    _class(new)

# root window
root = tk.Tk()
root.title('Dasboard Kalkulator')
root.geometry("900x400")

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create menus
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add menu items to the menus
file_menu.add_command(
    label='File Open', command=lambda: print("File Open function will be implemented here.")
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='Luas Balok', command=lambda: new_window(BalokCalculator)
)
app_menu.add_command(
    label='Luas Bola', command=lambda: new_window(BolaCalculator)
)
app_menu.add_command(
    label='Luas Kubus', command=lambda: new_window(KubusCalculator)
)
app_menu.add_command(
    label='Luas Limas Segiempat', command=lambda: new_window(LimasSegiempatCalculator)
)
app_menu.add_command(
    label='Luas Limas Segitiga', command=lambda: new_window(LimasSegitigaCalculator)
)
app_menu.add_command(
    label='Luas Prisma segitiga', command=lambda: new_window(PrismaSegitigaCalculator)
)
app_menu.add_command(
    label='Luas tabung', command=lambda: new_window(TabungCalculator)
)

# add the menus to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)

root.mainloop()
