import tkinter as tk 
from tkinter import ttk
import random
import time

root = tk.Tk()
root.title("Shorting Algorithm Visualizer")
root.maxsize(1500,1000)
root.config(bg="#90ccca")

algo_name = tk.StringVar()
algo_list = ["merge_sort" , "selection_sort" , "bubble_sort","insertion_sort"]

speed = tk.StringVar()
speed_list = ["slow","medium","fast"]

#ui 
display_window = tk.Frame(root, width= 900, height=300, bg="#c4e4e3")
display_window.grid(row=0, column=0, padx=5, pady=5)

lbl1 = tk.Label(display_window, text="Algorithm: ", bg="#90ccca")
lbl1.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

lbly = tk.Label(display_window, text="Array Size: ", bg="#90ccca")
lbly.grid(row=0, column=3, padx=10, pady=5, sticky=tk.W)

input = tk.IntVar()
inputsize = tk.Entry(display_window  , width=8, textvariable= input ,bg="#90ccca")
input.set(40)
inputsize.grid(row=1, column=3, padx=10, pady=5, sticky=tk.W)


algo_comboBox = ttk.Combobox(display_window, textvariable=algo_name, values=algo_list)
algo_comboBox.grid(row=0, column=1, padx=5, pady=5)
algo_comboBox.current(0)

lbl2 = tk.Label(display_window, text="Sorting Speed: ", bg="#90ccca")
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
speed_comboBox = ttk.Combobox(display_window, textvariable=speed, values=speed_list)
speed_comboBox.grid(row=1, column=1, padx=5, pady=5)
speed_comboBox.current(1)

canvas = tk.Canvas(root, width=800, height=400, bg="#c4e4e3")
canvas.grid(row=1, column=0, padx=10, pady=5)





#array = []

def display_arr(arr):
    canvas.delete("all")
    # tk.Canvas.size(1000,800)
    canvas_width = 800
    canvas_height = 400
    width_x = canvas_width / (len(arr)+1)
    temp_arr = [i / max(arr) for i in arr]
    for i in range(len(temp_arr)):
        x1 = i * width_x + 6
        y1 = canvas_height - temp_arr[i] * 390
        x2 = ( i + 1) * width_x + 2
        y2 = canvas_height
        canvas.create_rectangle(x1,y1,x2,y2,fill = "#90ccca")
    
    root.update_idletasks()

def generate():
    global array
    size = inputsize.get()
    array_size = int(size)
    array_begin = 10
    array_end = 200
    array = []
    for i in range(0 , array_size):
        random_integer = random.randint(array_begin,array_end)
        array.append(random_integer)
    
    display_arr(array)

def set_speed():
    slow = 0.5
    medium = 0.05
    fast = 0.00000001

    if speed_comboBox.get() == "slow":
        return slow
    elif speed_comboBox.get() == "medium":
        return medium
    elif speed_comboBox.get() == "fast":
        return fast
    
#algorithm
def merge(arr,begin,mid,end,display_arr):
    i = begin
    j = mid + 1 
    temp_array = []

    for k in range(begin , end + 1):
        if i > mid:
            temp_array.append(arr[j])
            j+=1
        elif j > end:
            temp_array.append(arr[i])
            i+=1
        elif arr[i] < arr[j]:
            temp_array.append(arr[i])
            i+=1
        else:
            temp_array.append(arr[j])
            j+=1
    for i in range(len(temp_array)):
        arr[begin] = temp_array[i]
        begin+=1

def merge_sort(array,begin ,end , display_arr , tym):
    if begin < end : 
        mid = int ( ( begin + end ) / 2)
        merge_sort(array, begin , mid  , display_arr , tym )
        merge_sort(array, mid +1 ,  end , display_arr , tym)
        merge(array, begin , mid , end , display_arr)

        display_arr(array)
        time.sleep(tym)

    display_arr(array)

#sorting algos 

def sort():
    tym = set_speed()
    length = len(array)

    if algo_comboBox.get() == "merge_sort":
        merge_sort(array,0,len(array)-1,display_arr,tym)

    elif algo_comboBox.get() == "selection_sort":
        for i in range(0 , length-1):
            for j in range(i +1 , length):
                if(array[i] > array[j]):
                    array[i],array[j] = array[j], array[i]
                    display_arr(array)
        display_arr(array)
    
    elif algo_comboBox.get() == "bubble_sort":
        for i in range(length-1):
            for j in range(0 , length - i -1 ):
                if(array[j] > array[j+1]):
                    array[j], array[j+1] = array[j+1], array[j]
                    display_arr(array)
        display_arr(array)
    
    elif algo_comboBox.get() == "insertion_sort": 
        for i in range(1, length):  
            a = array[i]  
            j = i - 1 
           
            while j >= 0 and a < array[j]:  
                array[j + 1] = array[j]  
                j -= 1 
                display_arr(array)

                 
            array[j + 1] = a
             
        display_arr(array) 
    
    
        



# checking .....
btn1 = tk.Button(display_window, text="Sort", command=sort, bg="#90ccca")
btn1.grid(row=4, column=1, padx=5, pady=5)


btn2 = tk.Button(display_window, text="Create Array", command=generate, bg="#90ccca")
btn2.grid(row=4, column=0, padx=5, pady=5)

    
root.mainloop()