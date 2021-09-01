from tkinter import Tk, Button, Label, filedialog
from gif import GIF
from sys import exit

class SelectMenu:
    Instance = None
    image = "./assets/wasans.gif"
    sound = "./assets/sans.wav"

    @staticmethod
    def init():
        if SelectMenu.Instance is None: SelectMenu.Instance = SelectMenu()
        return SelectMenu.Instance

    def _init(self):
        self.w = Tk()
        self.w.resizable(False, False)
        self.w.geometry("350x240+100+100")

        SelectMenu.Space(self.w, 2)
        Button(self.w, text="Image", command=self.getImage).pack()

        self.imageLabel = Label(self.w, text=self.image)
        self.imageLabel.pack()
        
        SelectMenu.Space(self.w, 1)
        Button(self.w, text="Sound", command=self.getSound).pack()
        
        self.soundLabel = Label(self.w, text=self.sound)
        self.soundLabel.pack()
        
        SelectMenu.Space(self.w, 1)
        Button(self.w, text="Start", command=self.destroy).pack()

        self.w.protocol("WM_DELETE_WINDOW", self.destroy_and_exit)
        
        return self.w
    
    def getImage(self):
        self.image = filedialog.askopenfilename(
            initialdir="/", title="Select file",
            filetypes=(("Image Files", ("*.gif", "*.png", "*.jpg")),)
        )
        self.imageLabel.configure(text=self.image)

    def getSound(self):
        self.sound = filedialog.askopenfilename(
            initialdir="/", title="Select file",
            filetypes=(("Sound Files", "*.wav"),)
        )
        self.soundLabel.configure(text=self.sound)

    @staticmethod
    def Space(w, size=1): Label(w, height=size).pack()

    def destroy(self):
        self.w.quit()
        self.w.destroy()

    def destroy_and_exit(self):
        self.destroy()
        exit()

SelectMenu.init()
