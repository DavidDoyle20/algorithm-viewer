import random
import time
class Drawable_Array:
    def __init__(self, win):
        self.array = list()
        self.win = win
        self.max_val = 0

    def set_array(self, array):
        self.array = array

    # Max not inclusive
    def generate_array(self, size=20, min_num=0, max_num=20, duplicates=True):
        self.array = []
        if duplicates:
            for i in range(size):
                self.array.append(random.randrange(min_num, max_num))
        else:
            if size > (max_num - min_num):
                raise Exception("Cant create an array with no duplicates")
            else:
                numbers = list(range(min_num, max_num))
                random.shuffle(numbers)
                for i in range(size):
                    self.array.append(numbers[i])
        print("Generated: ", self.array)
        self.max_val = max(self.array)
    
    def draw_array(self, color="cyan", display_numbers=False):
        for i in range(len(self.array)):
            self.draw_indexes(i, color=color, display_numbers=display_numbers)

    def selection_sort(self):
        if not self.array: return None

        for x in range(len(self.array)):
            self.draw_indexes(x, color="red")
            min_index = x
            for j in range(x+1, len(self.array)):
                self.draw_indexes(j, color="red")
                if self.array[j] < self.array[min_index]:
                    min_index = j
                self.draw_indexes(j, color="cyan", display_numbers=True)
            temp = self.array[x]
            self.array[x] = self.array[min_index]
            self.draw_indexes(x, color="SpringGreen2", display_numbers=True)
            self.array[min_index] = temp
            if min_index != x:
                self.draw_indexes(min_index, color="Cyan", display_numbers=True)

    def bubble_sort(self):
        if not self.array: return None
        n = len(self.array)

        for i in range(n-1):
            swapped = False

            for j in range(n-i-1):
                self.draw_indexes(j, j+1, color="red")
                if self.array[j] > self.array[j+1]:
                    swapped = True
                    temp = self.array[j]
                    self.array[j] = self.array[j+1]
                    self.array[j+1] = temp
                self.draw_indexes(j, j+1, color="cyan", display_numbers=True)
            if swapped == False:
                break
            self.draw_indexes(j+1, color="SpringGreen2", display_numbers=True)
    
    def insertion_sort(self):
        if not self.array: return None

        # Start with the second element
        # i represents the end of the sorted portion of the array
        for i in range(1, len(self.array)):
            # The key is an elment from the unsorted portion of the list
            self.draw_indexes(i, color="red", display_numbers=True)
            key = self.array[i]
            j = i - 1

            # Move elements for self.array[0..i-1], that are greater than key, to one position ahead of their current position
            # Loops backword from the midpoint and inserts the key in the correct position
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j] # Shifts element to the right
                self.draw_indexes(j, j + 1, color="SpringGreen2", display_numbers=True)
                j -= 1
            self.array[j + 1] = key # The position where the key needs to be inserted was found
            self.draw_indexes(j + 1, color="SpringGreen2", display_numbers=True)

    def merge_sort(self, left, right):
        def merge(left, mid, right):
            n1 = mid - left + 1
            n2 = right - mid
            
            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = self.array[left + i]
            for j in range(n2):
                R[j] = self.array[mid + 1 + j]
            
            i = 0
            j = 0
            k = left

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    self.array[k] = L[i]
                    self.draw_indexes(k, color="SpringGreen2", display_numbers=True)
                    i += 1
                else:
                    self.array[k] = R[j]
                    self.draw_indexes(k, color="SpringGreen2", display_numbers=True)
                    j += 1
                k += 1

            while i < n1:
                self.array[k] = L[i]
                self.draw_indexes(k, color="SpringGreen2", display_numbers=True)

                i += 1
                k += 1

            while j < n2:
                self.array[k] = R[j]
                self.draw_indexes(k, color="SpringGreen2", display_numbers=True)

                j += 1
                k += 1
                
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            merge(left, mid, right)


    # The QuickSort function implementation
    def quick_sort(self, low, high):
        def partition(low, high):
            # Choose the pivot
            pivot = self.array[high]
            self.draw_indexes(low, high, color="red", display_numbers=True)
            
            i = low - 1
            
            # Traverse arr[low..high] and move all smaller
            # elements on the left side. Elements from low to 
            # i are smaller after every iteration
            for j in range(low, high):
                if self.array[j] < pivot:
                    i += 1
                    self.array[i], self.array[j] = self.array[j], self.array[i]
                    self.draw_indexes(i, j, color="SpringGreen2", display_numbers=True)
                self.draw_indexes(i, j, color="cyan", display_numbers=True)
            
            # Move pivot after smaller elements and
            # return its position
            self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
            self.draw_indexes(i+1, high, color="SpringGreen2", display_numbers=True)
            return i + 1
        if low < high:
            # pi is the partition return index of pivot
            pi = partition(low, high)

            # Recursion calls for smaller elements
            # and greater or equals elements
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
            
    def draw_indexes(self, *args, color="orange", display_numbers=False):
        width = self.win.width
        height = self.win.height

        thickness = width/len(self.array)

        top_border = height - 20
        steps = int(top_border/self.max_val)

        print("Indexes ", args)
        for arg in args:
            x = thickness/2 + (arg * thickness)
            y = height - (self.array[arg]*steps)

            print(f"The x,y coords for {arg} are ({x},{y})")

            self.win.canvas.create_line(x, height, x, 0, fill=self.win.background_color, width=thickness)
            self.win.canvas.create_line(x, height, x, y, fill=color, width=thickness)
            if display_numbers:
                self.win.canvas.create_text(x, height-(self.array[arg]*steps)-10, text=f"{self.array[arg]}", width=thickness, font=("Helvetica", min(12,int(thickness/len(str(self.array[arg]))))))
        self.animate()
    
    def animate(self):
        self.win.redraw()
        time.sleep(0.05)


