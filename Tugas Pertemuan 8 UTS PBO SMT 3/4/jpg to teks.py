from PIL import Image, ImageTk
import pytesseract
import tkinter as tk
from tkinter import filedialog

def jpg_to_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def choose_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    if file_path:
        result_text.delete(1.0, tk.END)  # Bersihkan teks sebelumnya
        image = Image.open(file_path)
        display_image(image)
        text = jpg_to_text(file_path)
        result_text.insert(tk.END, text)

def display_image(image):
    # Resize image for display
    image.thumbnail((300, 300))
    tk_image = ImageTk.PhotoImage(image)
    image_label.config(image=tk_image)
    image_label.image = tk_image

# Membuat GUI
app = tk.Tk()
app.title("Image to Text Converter")

# Tombol untuk memilih gambar
choose_button = tk.Button(app, text="Choose Image", command=choose_image)
choose_button.pack(pady=10)

# Label untuk menampilkan gambar
image_label = tk.Label(app)
image_label.pack()

# TextBox untuk menampilkan teks hasil
result_text = tk.Text(app, height=10, width=50)
result_text.pack(pady=10)

app.mainloop()
