import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pygame
import threading
from PIL import Image, ImageTk, ImageEnhance
import time
import io
import eyed3

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("Media Player")
        self.master.geometry("300x400")  # Initial window size
        self.master.minsize(300, 300)  # Minimum window size
        self.master.configure(bg="#f0f0f0")

        self.current_file = None
        self.playing = False

        # Set icon
        icon_image = Image.open("folder.jpg")  # Change to the path of your icon file
        icon_image = icon_image.resize((30, 30), Image.ANTIALIAS)
        self.icon = ImageTk.PhotoImage(icon_image)
        self.master.iconphoto(False, self.icon)

        # Style for buttons
        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white")
        style.map("TButton", background=[("active", "#45a049")])

        # Frame for displaying cover image or video
        self.cover_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.cover_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Label for marquee (scrolling text)
        self.marquee_label = tk.Label(self.cover_frame, text="", bg="#f0f0f0", font=("Helvetica", 12))
        self.marquee_label.pack(expand=True, fill="x", padx=10, pady=5)
        self.marquee_label.place_forget()

        # Label for displaying cover image or video
        self.cover_label = tk.Label(self.cover_frame, bg="#f0f0f0", cursor="hand2")
        self.cover_label.pack(expand=True, fill="both")
        self.cover_label.bind("<Enter>", self.hover_enter)
        self.cover_label.bind("<Leave>", self.hover_leave)

        self.title_var = tk.StringVar()
        self.title_label = tk.Label(self.cover_frame, textvariable=self.title_var, bg="#f0f0f0", font=("Helvetica", 12), wraplength=300)
        self.title_label.pack(expand=True, fill="x", padx=10, pady=5)
        self.title_label.place_forget()

        self.position_scale = ttk.Progressbar(self.master, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.position_scale.pack(expand=True, fill="x", padx=10, pady=5)

        self.duration_label = tk.Label(self.master, text="Duration: 0:00", bg="#f0f0f0")
        self.duration_label.pack(expand=True, fill="x", padx=10, pady=5)

        # Frame for grouping buttons below the progress bar
        button_frame = tk.Frame(self.master, bg="#f0f0f0")
        button_frame.pack(expand=True, fill="x", padx=10, pady=10)

        # Tombol Play/Pause
        self.play_pause_button = ttk.Button(button_frame, text="▶ Play", command=self.toggle_play_pause, style="TButton")
        self.play_pause_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.stop_button = ttk.Button(button_frame, text="⏹ Stop", command=self.stop, style="TButton")
        self.stop_button.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        self.choose_file_button = ttk.Button(button_frame, text="Choose File", command=self.choose_file, style="TButton")
        self.choose_file_button.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        self.update_position_thread = threading.Thread(target=self.update_position)
        self.update_position_thread.daemon = True
        self.update_position_thread.start()

        # Bind the window resize event to adjust the layout
        self.master.bind("<Configure>", self.on_window_configure)

    def on_window_configure(self, event):
        # Update the position of the marquee and title labels when the window is resized
        if self.playing:
            self.hover_enter(None)

    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Media files", "*.mp3;*.mp4")])

        if file_path:
            self.current_file = file_path
            pygame.mixer.init()

            if file_path.lower().endswith('.mp3'):
                # MP3 File
                pygame.mixer.music.load(self.current_file)
                duration = pygame.mixer.Sound(self.current_file).get_length()
                self.position_scale.config(maximum=duration)
                self.duration_label.config(text=f"Duration: {self.format_time(duration)}")

                # Display cover from MP3 file
                cover_info = self.get_mp3_cover(self.current_file)
                self.display_cover(cover_info)

            elif file_path.lower().endswith('.mp4'):
                # MP4 File
                messagebox.showinfo("Info", "MP4 video will be displayed above the progress bar.")

    def toggle_play_pause(self):
        if self.playing:
            self.pause()
        else:
            self.play()

    def play(self):
        if self.current_file:
            pygame.mixer.music.play()
            self.playing = True
            self.play_pause_button.configure(text="⏸ Pause")

    def pause(self):
        pygame.mixer.music.pause()
        self.playing = False
        self.play_pause_button.configure(text="▶ Play")

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.play_pause_button.configure(text="▶ Play")
        self.position_scale.stop()

    def update_position(self):
        while True:
            if self.playing:
                position = pygame.mixer.music.get_pos() / 1000.0
                self.position_scale['value'] = position
            time.sleep(0.1)  # Update position every 0.1 seconds

    def format_time(self, seconds):
        minutes, seconds = divmod(int(seconds), 60)
        return f"{minutes}:{seconds:02}"

    def get_mp3_cover(self, mp3_file):
        try:
            audio = eyed3.load(mp3_file)
            if audio.tag and audio.tag.images:
                title = audio.tag.title if audio.tag.title else "Unknown Title"
                artist = audio.tag.artist if audio.tag.artist else "Unknown Artist"
                return title, artist, Image.open(io.BytesIO(audio.tag.images[0].image_data)).convert("RGBA")
            else:
                return None
        except Exception as e:
            print(f"Error retrieving MP3 cover: {e}")
            return None

    def display_cover(self, cover_info):
        if cover_info:
            title, artist, cover_image = cover_info

            # Set a maximum size for the displayed cover
            max_width, max_height = 300, 300
            cover_image.thumbnail((max_width, max_height))
            
            self.cover_image_original = ImageTk.PhotoImage(cover_image)
            self.cover_image_hover = ImageTk.PhotoImage(self.darken_image(cover_image, 0.5))

            self.cover_label.configure(image=self.cover_image_original, width=self.cover_image_original.width(), height=self.cover_image_original.height())
            self.cover_label.image = self.cover_image_original
            self.title_var.set(f"{title} - {artist}")  # Menampilkan judul dan artis
        else:
            # If no cover image, clear the label
            self.cover_label.configure(image=None, width=0, height=0)
            self.title_var.set("")

    def darken_image(self, img, factor):
        enhancer = ImageEnhance.Brightness(img)
        darkened_img = enhancer.enhance(factor)
        return darkened_img

    def hover_enter(self, event):
        # Darken the cover image, show marquee text, and set the title when the cursor enters the cover label with a smooth transition
        self.cover_label.configure(image=self.cover_image_hover)
        self.marquee_label.configure(text="Your Scrolling Text Here", width=self.cover_image_original.width())
        self.marquee_label.place(relx=0.5, rely=0.5, anchor="center", y=-50)  # Adjust the y-coordinate as needed
        self.title_label.place(relx=0.5, rely=0.5, anchor="center", y=50)  # Adjust the y-coordinate as needed

    def hover_leave(self, event):
        # Restore the original cover image, hide the marquee text, and hide the title when the cursor leaves the cover label with a smooth transition
        self.cover_label.configure(image=self.cover_image_original)
        self.marquee_label.place_forget()
        self.title_label.place_forget()

if __name__ == "__main__":
    root = tk.Tk()
    mp3_player = MP3Player(root)
    root.mainloop()
