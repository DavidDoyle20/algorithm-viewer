from window import Window
from drawable_array import Drawable_Array

def main():
    win = Window(500, 500)

    """
    dr = Drawable_Array(win=win)
    dr.generate_array(size=10,min_num=1, max_num=11, duplicates=False)
    dr.draw_array(display_numbers=True)
    dr.selection_sort()
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)
    dr.draw_array(display_numbers=True)
    dr.bubble_sort()
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)
    dr.draw_array(display_numbers=True)
    dr.insertion_sort()
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)
    dr.draw_array(display_numbers=True)
    dr.merge_sort(0, len(dr.array)-1)
    
    dr.quick_sort(0, len(dr.array)-1)
    """
    
    win.start()
    
main()