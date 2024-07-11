import tkinter as tk
from tkinter import filedialog
from PIL import Image
import pytesseract

# If Tesseract is not in your PATH, specify the installation path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff"), ("All files", "*.*")])
    if file_path:
        text = extract_text_from_image(file_path)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, text)

def save_to_file():
    text = text_box.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)

# Set up the GUI
root = tk.Tk()
root.title("Image to Text Extractor")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

open_button = tk.Button(frame, text="Open Image File", command=open_file)
open_button.pack(fill=tk.X)

text_box = tk.Text(frame, wrap=tk.WORD, width=60, height=20)
text_box.pack(pady=10)

save_button = tk.Button(frame, text="Save to Text File", command=save_to_file)
save_button.pack(fill=tk.X)

root.mainloop()
