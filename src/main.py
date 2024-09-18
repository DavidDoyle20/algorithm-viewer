from window import Window
from drawable_array import Drawable_Array

def main():
    win = Window(500, 500)

    dr = Drawable_Array(win=win)
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)

    dr.draw_array(display_numbers=True)
    #dr.selection_sort()
    #dr.bubble_sort()
    dr.insertion_sort()

    win.wait_for_close()
    
main()