# Calculate Py is a calculator made using Python and Tkinter. Created by Chris B. in 2020

from tkinter import *

root = Tk()
root.title("Calculate Py")

e = Entry(root, width=35, borderwidth=5) # Define the display box window?
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Where to put the display box?

def button_click(number):
    current = e.get() # get the current display box value
    e.delete(0, END) # delete the values that are showing up in the display box
    e.insert(0, str(current) + str(number)) # insert the new combined value into the display box

def button_clear(): # The function for clearing numbers from the display box
    e.delete(0, END)

def button_addition(): # The addition function details
    first_number = e.get() # Store the first entered number in this variable
    global f_num # create a global variable that can be used by the botton_equal() function
    f_num = int(first_number) 
    e.delete(0, END) # clear the display contents
    return

def button_equal():
    second_number = e.get() # store whatever number is in the display box
    e.delete(0, END) # clear the display box
    e.insert(0, f_num + int(second_number)) # insert the result
    
# Button dimensions and attributes for numbers 0 - 9, clear, add, etc. 
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=button_addition)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

# Button screen placement
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)


root.mainloop()

  
