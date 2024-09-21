from tkinter import Tk, BOTH, Canvas, ttk
from drawable_array import Drawable_Array

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.background_color = "gray75"
        self.array = Drawable_Array(win=self)

        self.root = Tk()
        self.root.title("Algorithm Viewer")

        self.frm = ttk.Frame(self.root)
        self.frm.pack(side='left')

        self.canvas = Canvas(self.root, width=width, height=height, background=self.background_color)
        self.canvas.pack(anchor='center', side='right', fill='both')

        self.generate_arr_btn = ttk.Button(self.frm, text="Generate Array", command=self.generate_array)
        self.generate_arr_btn.pack(padx=10, pady=10)

        self.selection_btn = ttk.Button(self.frm, text="Selection Sort", command=self.array.selection_sort)
        self.selection_btn.pack(padx=10, pady=10)

        self.bubble_btn = ttk.Button(self.frm, text="Bubble Sort", command=self.array.bubble_sort)
        self.bubble_btn.pack(padx=10, pady=10)

        self.insertion_btn = ttk.Button(self.frm, text="Insertion Sort", command=self.array.insertion_sort)
        self.insertion_btn.pack(padx=10, pady=10)

        self.merge_btn = ttk.Button(self.frm, text="Merge Sort", command=self.array.merge_sort)
        self.merge_btn.pack(padx=10, pady=10)

        self.quick_btn = ttk.Button(self.frm, text="Quick Sort", command=self.array.quick_sort)
        self.quick_btn.pack(padx=10, pady=10)

        # Connects the closing of the window "top left x" with the close mehtod
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        
    def generate_array(self):
        self.array.generate_array(size=20,min_num=1, max_num=21, duplicates=False)
        self.array.draw_array(display_numbers=True)

    def close(self):
        self.running = False
        self.root.quit()  # Stop the mainloop when the window is closed

    def start(self):
        self.generate_array()
        self.root.mainloop()  # Start the Tkinter main event loop
    
    def redraw(self):
        self.root.update()
        self.root.update_idletasks

    def draw_line(self, line, fill_color):
        line.draw(
            self.canvas, fill_color
        )

if __name__ == "__main__":
    window = Window(500,500)
    window.start()