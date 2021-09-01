from pynput.keyboard import Listener, Key
from pygame.mixer import init, Channel, Sound
from winoverlay import Window
from gif import GIF
from start import SelectMenu

n = SelectMenu.Instance
w = n._init()
w.mainloop()

init(frequency = 44100, size = -16, channels = 2, buffer = 1<<9)

c = [*map(Channel, range(5))]
i = 0
s = Sound(n.sound)

def play(_):
   global i
   c[i].play(s)
   i = (i+1)%(len(c))

w = Window(size=(1, 1))

gif = GIF.get(w.root, n.image)
gif.pack()

f = gif.frames[0]
w.size = f.width(), f.height()

with Listener(on_press=play) as l:
   gif.update()
   w.launch()
   l.join()
