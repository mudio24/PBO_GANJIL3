from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W

class FrmKelvinConverter:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Kelvin:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=0, column=1, padx=5, pady=5)  

        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5) 

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=3, column=1, padx=5, pady=5) 

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=4, column=1, padx=5, pady=5) 
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)

    def get_celcius(self, suhu):
        val = suhu - 273.15
        return val
    
    def get_fahrenheit(self, suhu):
        val = (suhu - 273.15) * 9/5 + 32
        return val
    
    def get_reamur(self, suhu):
        val = (suhu - 273.15) * 4/5
        return val

    def onHitung(self):
        # Suhu dalam Kelvin
        suhu = float(self.txtKelvin.get())
        C = self.get_celcius(suhu)
        F = self.get_fahrenheit(suhu)
        R = self.get_reamur(suhu)

        self.txtCelcius.delete(0, END)
        self.txtCelcius.insert(END, str(C))

        self.txtFahrenheit.delete(0, END)
        self.txtFahrenheit.insert(END, str(F))

        self.txtReamur.delete(0, END)
        self.txtReamur.insert(END, str(R))
        
    def onKeluar(self, event=None):
        self.parent.destroy()            

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmKelvinConverter(root, "Program Konversi Suhu Kelvin")
    root.mainloop()
