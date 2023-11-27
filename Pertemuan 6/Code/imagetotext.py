import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

class ImageToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        # Set the path to the Tesseract executable
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Create and pack widgets
        self.create_widgets()

    def create_widgets(self):
        # Image display
        self.image_label = tk.Label(self.root)
        self.image_label.pack(pady=10)

        # Select image button
        select_button = tk.Button(self.root, text="Select Image", command=self.load_image)
        select_button.pack(pady=10)

        # Convert button
        convert_button = tk.Button(self.root, text="Convert to Text", command=self.convert_to_text)
        convert_button.pack(pady=10)

        # Text display
        self.text_label = tk.Label(self.root, wraplength=400, justify=tk.LEFT)
        self.text_label.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.display_image(file_path)

    def display_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)

        self.image_label.configure(image=photo)
        self.image_label.image = photo

        self.image_path = file_path

    def convert_to_text(self):
        if hasattr(self, 'image_path') and self.image_path:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image)
            self.text_label.config(text=text)
        else:
            self.text_label.config(text="Please select an image first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextApp(root)
    root.mainloop()
