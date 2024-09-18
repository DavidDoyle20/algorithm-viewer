from tkinter import Tk, BOTH, Canvas, ttk

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = "gray75"

        self.root = Tk()
        self.root.title("Algorithm Viewer")
        self.root.geometry(f"{self.width}x{self.height}")
        self.canvas = Canvas(self.root, width=width, height=height, background=self.background_color)

        self.canvas.pack(anchor='center')
        self.running = False
        # Connects the closing of the window "top left x" with the close mehtod
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update()
        self.root.update_idletasks

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(
            self.canvas, fill_color
        )