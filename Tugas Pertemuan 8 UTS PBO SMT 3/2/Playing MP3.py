import pygame
from tkinter import Tk, filedialog, Label, Button

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("400x200")

        self.file_path = None

        self.init_ui()

    def init_ui(self):
        Label(self.master, text="MP3 Player", font=("Helvetica", 16)).pack(pady=10)

        Button(self.master, text="Choose MP3 File", command=self.choose_file).pack(pady=10)
        Button(self.master, text="Play", command=self.play_music).pack(pady=5)
        Button(self.master, text="Stop", command=self.stop_music).pack(pady=5)

    def choose_file(self):
        self.file_path = filedialog.askopenfilename(title="Choose a MP3 file", filetypes=[("MP3 files", "*.mp3")])

    def play_music(self):
        if self.file_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.file_path)
            pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

def main():
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
