import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Responsive Video Player")
        self.root.geometry("800x600")

        # Tambahkan binding untuk perubahan ukuran window
        self.root.bind("<Configure>", self.resize_video)

        self.create_widgets()

    def create_widgets(self):
        # Frame untuk menempatkan tombol-tombol
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.BOTTOM, pady=10)

        # Tombol untuk memilih file video
        select_button = tk.Button(control_frame, text="Pilih Video", command=self.select_video)
        select_button.pack(side=tk.LEFT, padx=10)

        # Tombol untuk memulai pemutaran video
        play_button = tk.Button(control_frame, text="Mainkan", command=self.play_video)
        play_button.pack(side=tk.LEFT, padx=10)

        # Tombol untuk menghentikan pemutaran video
        stop_button = tk.Button(control_frame, text="Stop", command=self.stop_video)
        stop_button.pack(side=tk.LEFT, padx=10)

        # Label untuk menampilkan status
        self.status_label = tk.Label(control_frame, text="")
        self.status_label.pack(side=tk.LEFT, padx=10)

        # Inisialisasi variabel video
        self.video_path = None
        self.video_capture = None

    def select_video(self):
        # Memilih file video
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        if file_path:
            self.video_path = file_path
            self.status_label.config(text=f"File Video: {file_path}")

    def play_video(self):
        if self.video_path:
            # Menghentikan video yang sedang diputar sebelumnya
            self.stop_video()

            # Membuka file video
            self.video_capture = cv2.VideoCapture(self.video_path)

            # Mendapatkan informasi video
            self.fps = int(self.video_capture.get(cv2.CAP_PROP_FPS))

            # Membuat frame untuk menampilkan video
            self.video_frame = tk.Label(self.root)
            self.video_frame.pack(expand=True, fill="both")

            # Fungsi untuk membaca dan menampilkan setiap frame video
            def update_frame():
                ret, frame = self.video_capture.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = self.resize_frame(frame)
                    img = self.convert_frame_to_image(frame)
                    self.video_frame.configure(image=img)
                    self.video_frame.img = img
                    self.root.after(1000 // self.fps, update_frame)
                else:
                    self.stop_video()

            # Memulai pemutaran video
            update_frame()

            # Memainkan audio
            audio_path = self.video_path
            audio = AudioSegment.from_file(audio_path)
            play(audio)

    def resize_frame(self, frame):
        # Mengubah ukuran frame video sesuai dengan ukuran window
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Menyesuaikan ukuran frame dengan ukuran window
        if window_width > 1 and window_height > 1:
            frame = cv2.resize(frame, (window_width, window_height))

        return frame

    def convert_frame_to_image(self, frame):
        # Konversi frame OpenCV menjadi format yang dapat ditampilkan di Tkinter
        img = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=img)
        return img

    def stop_video(self):
        # Menghentikan pemutaran video
        if self.video_capture is not None:
            self.video_capture.release()
            self.video_frame.pack_forget()

    def resize_video(self, event):
        # Mengubah ukuran frame video sesuai dengan ukuran window
        if hasattr(self, 'video_capture') and self.video_capture is not None:
            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = self.resize_frame(frame)
                img = self.convert_frame_to_image(frame)
                self.video_frame.configure(image=img)
                self.video_frame.img = img

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayer(root)
    root.mainloop()
