from window import Window
from drawable_array import Drawable_Array

def main():
    win = Window(1000, 1000)

    dr = Drawable_Array(win=win)
    dr.generate_array(size=200,min_num=1, max_num=201, duplicates=False)
    dr.draw_array(display_numbers=True)
    """
    dr.selection_sort()
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)
    dr.draw_array(display_numbers=True)
    dr.bubble_sort()
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)
    dr.draw_array(display_numbers=True)
    dr.insertion_sort()
    dr.generate_array(size=50,min_num=1, max_num=51, duplicates=False)
    dr.draw_array(display_numbers=True)
    """
    dr.merge_sort(0, len(dr.array)-1)
    """
    dr.quick_sort(0, len(dr.array)-1)
    """
    win.wait_for_close()
    
main()