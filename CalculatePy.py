# Calculate Py is a calculator made using Python. Created by Chris B. in 2020

from tkinter import * 
from math import sqrt

root = Tk()
root.title("Calculate Py")
root.resizable(False, False)

e = Entry(root, width=55, borderwidth=10)
e.grid(row=0, column=0, columnspan=4, pady=20)

def operation(opr):
    global f_num # create a global variable f_num that can be used by the botton_equal() function
    f_num = float(e.get()) 
    global math # create a global variable math that can be used by the botton_equal() function
    math = opr
    e.delete(0, END)

def button_click(number):
    current = e.get() 
    e.delete(0, END) 
    e.insert(0, str(current) + str(number)) # insert the new combined value into the display box

def button_clear():
    e.delete(0, END)

def button_xsquared():
    first_num = float(e.get())
    e.delete(0, END)
    e.insert(0, round((first_num ** 2),4))

def button_sqrt():
    first_num = float(e.get())
    try:
        e.delete(0, END)
        e.insert(0, round((sqrt(first_num)),4))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Cannot calculate the square root of a negative number")

def button_equal():
    second_num = float(e.get())
    e.delete(0, END)
    try:
        if math == "addition":
            e.insert(0, round((f_num + second_num),4)) 
        elif math == "subtraction":
            e.insert(0, round((f_num - second_num),4)) 
        elif math == "multiplication":
            e.insert(0, round((f_num * second_num),4)) 
        elif math == "division":
            e.insert(0, round((f_num / second_num),4))
    except:
        e.insert(0,"An error occured")
    
# Button size, attributes, and location for button clicks like numbers 0 - 9 and the decimal sign
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1)).grid(row=4, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2)).grid(row=4, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3)).grid(row=4, column=2)
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4)).grid(row=3, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5)).grid(row=3, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6)).grid(row=3, column=2)
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7)).grid(row=2, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8)).grid(row=2, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9)).grid(row=2, column=2)
button_0 = Button(root, text="0", padx=87, pady=20, command=lambda: button_click(0)).grid(row=5, column=0, columnspan=2)
button_decimal = Button(root, text=".", padx=42, pady=20, command=lambda: button_click(".")).grid(row=5, column=2)

# Button size, attributes, and location for operation buttons
button_add = Button(root, text="+", padx=38, pady=20, command=lambda: operation("addition")).grid(row=4, column=3)
button_subtact = Button(root, text="-", padx=40, pady=20, command=lambda: operation("subtraction")).grid(row=3, column=3)
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: operation("multiplication")).grid(row=2, column=3)
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: operation("division")).grid(row=1, column=3)
button_equal = Button(root, text="=", padx=38, pady=20, command=button_equal).grid(row=5, column=3)
button_clear = Button(root, text="C", padx=39, pady=20, command=button_clear).grid(row=1, column=0)
button_xsquared = Button(root, text="x\N{SUPERSCRIPT TWO}", padx=39, pady=20, command=button_xsquared).grid(row=1, column=2)
button_sqrt = Button(root, text="\N{SQUARE ROOT}", padx=39, pady=20, command=button_sqrt).grid(row=1, column=1)

root.mainloop()
