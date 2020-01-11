# Calculate Py is a calculator made using Python and Tkinter. Created by Chris B. in 2020

from tkinter import * 
from math import sqrt

root = Tk()
root.title("Calculate Py")
root.resizable(False, False)
root.config(bg="black")

e = Entry(root, width=15, borderwidth=10, relief=FLAT)
e.grid(row=0, column=0, columnspan=4, pady=40)
e.config(font = ("Consolas", 18, "bold"))

def error():
    e.delete(0, END)
    e.insert(0, 'Click "C"')    

def operation(opr):
    try:
        global f_num
        f_num = float(e.get()) 
        global math 
        math = opr
        e.delete(0, END)
    except:
        f_num = 0.0
        math = "none"
        error()

def button_click(number):
    try:
        current = e.get() 
        e.delete(0, END) 
        e.insert(0, str(current) + str(number))
    except:
        error()

def button_clear():
    e.delete(0, END)

def button_xsquared():
    try:
        first_num = float(e.get())
        e.delete(0, END)
        e.insert(0, round((first_num ** 2),4))
    except:
        error()

def button_sqrt():
    try:
        first_num = float(e.get())
        e.delete(0, END)
        e.insert(0, round((sqrt(first_num)),4))
    except:
        error()

def button_equal():
    try:
        second_num = float(e.get())
        e.delete(0, END)
        if math == "addition":
            e.insert(0, round((f_num + second_num),4)) 
        elif math == "subtraction":
            e.insert(0, round((f_num - second_num),4)) 
        elif math == "multiplication":
            e.insert(0, round((f_num * second_num),4)) 
        elif math == "division":
            e.insert(0, round((f_num / second_num),4))
    except:
        error()
    
### Button size, attributes, and location for button clicks like numbers 0 - 9 and the decimal sign ###
font_type = "Consolas"
font_size = 14
x = 20
y = 10

button_1 = Button(root, text="1", padx=x, pady=y, command=lambda: button_click(1))
button_1.grid(row=4, column=0)
button_1.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_2 = Button(root, text="2", padx=x, pady=y, command=lambda: button_click(2))
button_2.grid(row=4, column=1)
button_2.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_3 = Button(root, text="3", padx=x, pady=y, command=lambda: button_click(3))
button_3.grid(row=4, column=2)
button_3.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_4 = Button(root, text="4", padx=x, pady=y, command=lambda: button_click(4))
button_4.grid(row=3, column=0)
button_4.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_5 = Button(root, text="5", padx=x, pady=y, command=lambda: button_click(5))
button_5.grid(row=3, column=1)
button_5.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_6 = Button(root, text="6", padx=x, pady=y, command=lambda: button_click(6))
button_6.grid(row=3, column=2)
button_6.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_7 = Button(root, text="7", padx=x, pady=y, command=lambda: button_click(7))
button_7.grid(row=2, column=0)
button_7.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_8 = Button(root, text="8", padx=x, pady=y, command=lambda: button_click(8))
button_8.grid(row=2, column=1)
button_8.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_9 = Button(root, text="9", padx=x, pady=y, command=lambda: button_click(9))
button_9.grid(row=2, column=2)
button_9.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_0 = Button(root, text="0", padx=55, pady=10, command=lambda: button_click(0))
button_0.grid(row=5, column=0, columnspan=2)
button_0.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

button_decimal = Button(root, text=".", padx=x, pady=y, command=lambda: button_click("."))
button_decimal.grid(row=5, column=2)
button_decimal.config(relief=FLAT, bg="black", fg="white", font = (font_type, font_size, "bold"))

### Button size, attributes, and location for operation buttons ###
button_add = Button(root, text="+", padx=x, pady=y, command=lambda: operation("addition"))
button_add.grid(row=4, column=3)
button_add.config(relief=FLAT, bg="black", fg="#0C7BDC", font = (font_type, font_size, "bold"))

button_subtact = Button(root, text="-", padx=x, pady=y, command=lambda: operation("subtraction"))
button_subtact.grid(row=3, column=3)
button_subtact.config(relief=FLAT, bg="black", fg="#0C7BDC", font = (font_type, font_size, "bold"))

button_multiply = Button(root, text="*", padx=x, pady=y, command=lambda: operation("multiplication"))
button_multiply.grid(row=2, column=3)
button_multiply.config(relief=FLAT, bg="black", fg="#0C7BDC", font = (font_type, font_size, "bold"))

button_divide = Button(root, text="/", padx=x, pady=y, command=lambda: operation("division"))
button_divide.grid(row=1, column=3)
button_divide.config(relief=FLAT, bg="black", fg="#0C7BDC", font = (font_type, font_size, "bold"))

button_equal = Button(root, text="=", padx=x, pady=y, command=button_equal)
button_equal.grid(row=5, column=3)
button_equal.config(relief=FLAT, bg="black", fg="#FFC20A", font = (font_type, font_size, "bold"))

button_clear = Button(root, text="C", padx=x, pady=y, command=button_clear)
button_clear.grid(row=1, column=0)
button_clear.config(relief=FLAT, bg="black", fg="#FFC20A", font = (font_type, font_size, "bold"))

button_xsquared = Button(root, text="x\N{SUPERSCRIPT TWO}", padx=14, pady=10, command=button_xsquared)
button_xsquared.grid(row=1, column=2)
button_xsquared.config(relief=FLAT, bg="black", fg="#0C7BDC", font = (font_type, font_size, "bold"))

button_sqrt = Button(root, text="\N{SQUARE ROOT}", padx=x, pady=y, command=button_sqrt)
button_sqrt.grid(row=1, column=1)
button_sqrt.config(relief=FLAT, bg="black", fg="#0C7BDC", font = (font_type, font_size, "bold"))

root.mainloop()
