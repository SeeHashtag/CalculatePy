# Calculate Py is a calculator made using Python and Tkinter. Created by Chris B. in 2020

print("""
Instructions:
1. Enter a number.
2. Enter an operation (+, -, *, **, /, %, or //).
3. Enter another number.
""")
num1 = float(input("Enter a number: "))
oper = str(input("Enter an operation: "))
num2 = float(input("Enter a number: "))

try:
    if oper == "+":
        result = str(num1 + num2)
        print(num1, "+", num2, "=", result)
    elif oper == "-":
        result = str(num1 - num2)
        print(num1, "-", num2, "=", result)   
    elif oper == "*":
        result = str(num1 * num2)
        print(num1, "*", num2, "=", result)
    elif oper == "/":
        result = str(num1 / num2)
        print(num1, "/", num2, "=", result)
    elif oper == "%":
        result = str(num1 % num2)
        print(num1, "%", num2, "=", result)
    elif oper == "**":
        result = str(num1 ** num2)
        print(num1, "^", num2, "=", result)
    elif oper == "//":
        result = str(num1 // num2)
        print(num1, "//", num2, "=", result)
    else:
        print("Unknown input")
except:
    print("An error occured")
