from tkinter import PhotoImage, Label

class GIF:
    @staticmethod
    def getFrame(file):
        i = 0
        res = []
        while 1:
            try: res.append(PhotoImage(file=file, format=f'gif -index {i}'))
            except: break
            i += 1
        return res, i

    @staticmethod
    def get(root, file, speed=1):
        if any(map(file.__contains__, ['.jpg', '.png'])):
            return Label(root, image=PhotoImage(file=file))
        return GIF(root, file, speed)
    
    def __init__(self, root, file, speed=1):
        self.frames, self.frame = GIF.getFrame(file)
        self.idx = 0
        self.root = root
        self.speed = speed
        self.label = Label(root)
        
    def update(self):
        self.idx = (self.idx+1)%self.frame
        self.label.configure(image = self.frames[self.idx])
        update = self.update
        self.root.after(100*self.speed, update)

    def pack(self):
        self.label.pack()
