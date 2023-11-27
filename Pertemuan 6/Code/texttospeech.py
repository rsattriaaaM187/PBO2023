import tkinter as tk
from tkinter import ttk
import pyttsx3

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech")

        # Label
        self.label = ttk.Label(root, text="Masukkan Teks:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        # Entry untuk memasukkan teks
        self.text_entry = ttk.Entry(root, width=40)
        self.text_entry.grid(row=0, column=1, padx=10, pady=10)

        # Tombol untuk memutar suara
        self.button = ttk.Button(root, text="Putar Suara", command=self.text_to_speech)
        self.button.grid(row=1, column=0, columnspan=2, pady=10)

    def text_to_speech(self):
        # Mengambil teks dari entry
        text_to_convert = self.text_entry.get()

        # Inisialisasi mesin text-to-speech
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Kecepatan bicara, bisa diubah sesuai kebutuhan
        engine.say(text_to_convert)
        engine.runAndWait()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()
