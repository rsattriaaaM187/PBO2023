import tkinter as tk

class Kelvin:
    def __init__(self, suhu):
        self.suhu = suhu

    def get_kelvin(self):
        return self.suhu

    def get_celsius(self):
        return self.suhu - 273

    def get_fahrenheit(self):
        return (9/5 * (self.suhu - 273)) + 32

    def get_reamur(self):
        return (4/5 * (self.suhu - 273))

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Converter Suhu Kelvin")

        self.label_kelvin = tk.Label(root, text="Kelvin:")
        self.label_kelvin.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_kelvin = tk.Entry(root)
        self.entry_kelvin.grid(row=0, column=1, padx=10, pady=10)

        self.button_convert = tk.Button(root, text="Convert", command=self.convert)
        self.button_convert.grid(row=0, column=2, padx=10, pady=10)

        self.label_celsius = tk.Label(root, text="Celsius:")
        self.label_celsius.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.entry_celsius = tk.Entry(root, state="readonly")
        self.entry_celsius.grid(row=1, column=1, padx=10, pady=10)

        self.label_fahrenheit = tk.Label(root, text="Fahrenheit:")
        self.label_fahrenheit.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.entry_fahrenheit = tk.Entry(root, state="readonly")
        self.entry_fahrenheit.grid(row=2, column=1, padx=10, pady=10)

        self.label_reamur = tk.Label(root, text="Reamur:")
        self.label_reamur.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.entry_reamur = tk.Entry(root, state="readonly")
        self.entry_reamur.grid(row=3, column=1, padx=10, pady=10)

    def convert(self):
        try:
            kelvin = float(self.entry_kelvin.get())
            K = Kelvin(kelvin)
            celsius = K.get_celsius()
            fahrenheit = K.get_fahrenheit()
            reamur = K.get_reamur()

            self.entry_celsius.config(state="normal")
            self.entry_celsius.delete(0, tk.END)
            self.entry_celsius.insert(0, celsius)
            self.entry_celsius.config(state="readonly")

            self.entry_fahrenheit.config(state="normal")
            self.entry_fahrenheit.delete(0, tk.END)
            self.entry_fahrenheit.insert(0, fahrenheit)
            self.entry_fahrenheit.config(state="readonly")

            self.entry_reamur.config(state="normal")
            self.entry_reamur.delete(0, tk.END)
            self.entry_reamur.insert(0, reamur)
            self.entry_reamur.config(state="readonly")
        except ValueError:
            self.clear_entries()
            self.result_label.config(text="Masukkan suhu dalam bentuk numerik.")

    def clear_entries(self):
        self.entry_celsius.config(state="normal")
        self.entry_celsius.delete(0, tk.END)
        self.entry_celsius.config(state="readonly")

        self.entry_fahrenheit.config(state="normal")
        self.entry_fahrenheit.delete(0, tk.END)
        self.entry_fahrenheit.config(state="readonly")

        self.entry_reamur.config(state="normal")
        self.entry_reamur.delete(0, tk.END)
        self.entry_reamur.config(state="readonly")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
