from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

class CalculatorApp(MDApp):
    def build(self):
        self.title = "Aplikasi Menghitung Luas Dan Volume Balok"
        self.theme_cls.primary_palette = "Blue"

        layout = MDScreen()

        # Title Labels
        title_box = MDGridLayout(cols=1, size_hint=(None, None), width=300, height=100, pos_hint={'center_x': 0.5, 'center_y': 0.9})
        title_label = MDLabel(
            text="Hitung Luas Dan Volume Balok",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )
        title_box.add_widget(title_label)
        layout.add_widget(title_box)

        # Input Fields
        input_box = MDGridLayout(cols=1, size_hint=(None, None), width=300, height=250, pos_hint={'center_x': 0.5, 'center_y': 0.6})

        self.panjang_text = MDTextField(
            hint_text="Panjang (cm)",
            helper_text="Enter the length",
            helper_text_mode="on_focus",
            input_type="number"
        )
        self.lebar_text = MDTextField(
            hint_text="Lebar (cm)",
            helper_text="Enter the width",
            helper_text_mode="on_focus",
            input_type="number"
        )
        self.tinggi_text = MDTextField(
            hint_text="Tinggi (cm)",
            helper_text="Enter the height",
            helper_text_mode="on_focus",
            input_type="number"
        )

        input_box.add_widget(self.panjang_text)
        input_box.add_widget(self.lebar_text)
        input_box.add_widget(self.tinggi_text)

        layout.add_widget(input_box)

        # Buttons
        button_box = MDGridLayout(cols=2, spacing=10, size_hint=(None, None), width=300, height=50, pos_hint={'center_x': 0.5, 'center_y': 0.44})

        calculate_button = MDRaisedButton(text="Calculate")
        calculate_button.bind(on_release=self.calculate)

        reset_button = MDRaisedButton(text="Reset")
        reset_button.bind(on_release=self.reset)

        button_box.add_widget(calculate_button)
        button_box.add_widget(reset_button)

        layout.add_widget(button_box)

        # Result Labels
        result_box = MDGridLayout(cols=1, size_hint=(None, None), width=500, height=200, pos_hint={'center_x': 0.5, 'center_y': 0.38})

        self.luas_permukaan_label = MDLabel(
            text="Luas Permukaan:",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )
        self.volume_label = MDLabel(
            text="Volume:",
            halign="center",
            theme_text_color="Primary",
            font_style="H6"
        )

        # Output Labels
        self.panjang_label = MDLabel()
        self.lebar_label = MDLabel()
        self.tinggi_label = MDLabel()
        self.output_label = MDLabel()

        result_box.add_widget(self.panjang_label)
        result_box.add_widget(self.lebar_label)
        result_box.add_widget(self.tinggi_label)
        result_box.add_widget(self.luas_permukaan_label)
        result_box.add_widget(self.volume_label)
        result_box.add_widget(self.output_label)

        layout.add_widget(result_box)

        return layout

    def calculate(self, instance):
        try:
            panjang = float(self.panjang_text.text)
            lebar = float(self.lebar_text.text)
            tinggi = float(self.tinggi_text.text)
            luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
            volume = panjang * lebar * tinggi
            self.luas_permukaan_label.text = f"Luas Permukaan: {luas_permukaan:.2f} cm^2"
            self.volume_label.text = f"Volume: {volume:.2f} cm^3"
            self.output_label.text = ""
        except ValueError:
            self.luas_permukaan_label.text = "Error: Invalid input"
            self.volume_label.text = "Volume:"

    def reset(self, instance):
        self.panjang_text.text = ""
        self.lebar_text.text = ""
        self.tinggi_text.text = ""
        self.luas_permukaan_label.text = "Luas Permukaan:"
        self.volume_label.text = "Volume:"
        self.output_label.text = ""

if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
