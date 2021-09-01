# Original code by David Ma
# https://github.com/davidmaamoaix/overlay

from tkinter import Tk, Toplevel

overlays = []

master = Tk()
master.withdraw()

TRANSPARENT = '#000001'

class Window:
    def __init__(self, **kwargs):
        self._root = Toplevel()

        self._root.overrideredirect(1)
        self._root.update_idletasks()
        self._root.lift()

        self.size = kwargs.get('size', (500, 250))
        self.position = kwargs.get('position', (0, 0))
        self.transparent = kwargs.get('transparent', False)

        self.draggable = kwargs.get('draggable', True)
        self._root.bind('<ButtonPress-1>', self._drag_start)
        self._root.bind('<ButtonRelease-1>', self._drag_stop)
        self._root.bind('<B1-Motion>', self._move)
        self._drag_stop(None)

        self._root.wm_attributes('-topmost', True)
        self._root.wm_attributes('-transparent', TRANSPARENT)

        overlays.append(self)

    def focus(self):
        self._root.focus_force()

    def center(self):
        w, h = self._root.winfo_screenwidth(), self._root.winfo_screenheight()

        center_x = w / 2
        center_y = h / 2
        offset_x, offset_y = tuple(map(lambda x: x / 2, self.size))
        new_x = center_x - offset_x
        new_y = center_y - offset_y - h//7.5
        self.position = new_x, new_y

    def hide(self):
        '''Hide this overlay.'''
        self._root.withdraw()

    def show(self):
        '''Show this overlay.'''
        self._root.wm_deiconify()
        self._root.lift()
        self._root.wm_attributes('-topmost', True)

    def destroy(self):
        '''Destroy this overlay.'''
        self._root.destroy()

    def _drag_start(self, event):
        '''The start of moving this overlay.'''
        self.x = event.x
        self.y = event.y

    def _drag_stop(self, event):
        '''The start of moving the overlay.'''
        self.x = None
        self.y = None

    def _move(self, event):
        '''The handler for moving the overlay.'''
        if self.draggable:
            mouse_x = self._root.winfo_pointerx() - self._root.winfo_rootx()
            mouse_y = self._root.winfo_pointery() - self._root.winfo_rooty()
            new_x = self._root.winfo_x() + mouse_x - self.x
            new_y = self._root.winfo_y() + mouse_y - self.y
            self.position = new_x, new_y

    @property
    def root(self):
        return self._root

    @property
    def size(self):
        return self._size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, newPos):
        self._position = tuple(map(lambda x: int(x), newPos))
        self._root.geometry('+%s+%s'%self._position)

    @size.setter
    def size(self, newSize):
        self._size = tuple(map(lambda x: int(x), newSize))
        self._root.geometry('%sx%s'%self._size)

    @property
    def transparent(self):
        return self._root['bg'] == TRANSPARENT

    @transparent.setter
    def transparent(self, newTransparent):
        bg = TRANSPARENT if newTransparent else 'white'
        self._root.config(bg=bg)

    @staticmethod
    def after(milliseconds, func, *args):
        '''Runs the given function with the given args after launch.'''
        master.after(milliseconds, func, *args)

    @staticmethod
    def launch():
        '''Enter the mainloop for the collection of all overlays.'''
        master.mainloop()

    @staticmethod
    def hide_all():
        '''Hide all overlays.'''
        for overlay in overlays:
            overlay.hide()

    @staticmethod
    def show_all():
        '''Show all overlays.'''
        for overlay in overlays:
            overlay.show()

    @staticmethod
    def destroy_all():
        '''Destroy all overlays and end the mainloop.'''
        for overlay in overlays:
            overlay.destroy()
        overlays = []

        master.destroy()
