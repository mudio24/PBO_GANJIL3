import tkinter as tk
from tkinter import ttk

def convert_temperature():
    try:
        # Mengambil nilai suhu dari input pengguna
        temperature = float(entry.get())

        # Memilih unit suhu yang dipilih oleh pengguna
        unit = unit_var.get()

        # Melakukan konversi suhu
        if unit == "Celsius":
            result = temperature
        elif unit == "Fahrenheit":
            result = (temperature * 9/5) + 32
        elif unit == "Reamur":
            result = temperature * 4/5
        elif unit == "Kelvin":
            result = temperature + 273.15

        # Menampilkan hasil konversi di dalam textbox
        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, f"Result: {result:.2f} {unit}")
        result_textbox.config(state=tk.DISABLED)
    except ValueError:
        result_textbox.config(state=tk.NORMAL)
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, "Invalid input. Please enter a number.")
        result_textbox.config(state=tk.DISABLED)

# Membuat instance Tkinter
app = tk.Tk()
app.title("Temperature Converter")
app.geometry("400x300")  # Ukuran jendela

# Frame utama
main_frame = ttk.Frame(app, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Membuat label dan entry untuk input suhu
label = ttk.Label(main_frame, text="Enter Temperature:")
label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry = ttk.Entry(main_frame)
entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

# Membuat dropdown untuk memilih unit suhu
unit_var = tk.StringVar()
unit_var.set("Celsius")  # Default unit suhu

unit_label = ttk.Label(main_frame, text="Choose Unit:")
unit_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

unit_dropdown = ttk.Combobox(main_frame, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Reamur", "Kelvin"])
unit_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
unit_dropdown.current(0)  # Set nilai default

# Tombol konversi suhu
convert_button = ttk.Button(main_frame, text="Convert", command=convert_temperature)
convert_button.grid(row=2, column=0, columnspan=2, pady=20)

# Menampilkan hasil konversi suhu di dalam textbox
result_textbox = tk.Text(main_frame, height=2, state=tk.DISABLED, wrap=tk.WORD)
result_textbox.grid(row=3, column=0, columnspan=2, pady=10, sticky=tk.W)

app.geometry("680x350")

# Menjalankan aplikasi Tkinter
app.mainloop()
