import tkinter


class PaintApp(tkinter.Tk):
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.resizable(False, False)
        c = tkinter.Canvas(self, bg='white')
        c.bind("<B1-Motion>", lambda event: c.create_oval(event.x, event.y, event.x, event.y, fill="green", width=5))
        c.pack()
