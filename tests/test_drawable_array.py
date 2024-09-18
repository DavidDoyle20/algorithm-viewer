import unittest
from src.drawable_array import Drawable_Array

class TestDrawableArray(unittest.TestCase):
    def test_set_array(self):
        arr = Drawable_Array(None)
        lst = [1,5,3]
        arr.set_array(lst)
        self.assertEqual(arr.array, lst)
    def test_generate_array_default(self):
        arr = Drawable_Array(None)
        arr.generate_array()
        self.assertEqual(20, len(arr.array))
    def test_generate_array_no_duplicates(self):
        arr = Drawable_Array(None)
        arr.generate_array(duplicates=False)
        duplicate_set = set(arr.array)
        self.assertEqual(len(duplicate_set), len(arr.array))
    def test_generate_array_size_too_large(self):
        arr = Drawable_Array(None)
        with self.assertRaises(Exception):
            arr.generate_array(size=100, duplicates=False)

            
if __name__=='__main__':
    unittest.main()
        

