# Calculate Py is a calculator made using Python. Created by Chris B. in 2020

print("Options:")
print("Enter 'add' to add two numbers")
print("Enter 'subtract' to subtract two numbers")
print("Enter 'multiply' to multiply two numbers")
print("Enter 'exponent' to raise the first number to the second numbers")
print("Enter 'divide' to divide two numbers")
print("Enter 'remainder' to divide two numbers and get the remainder only")
print("Enter 'floor' to divide two numbers and get the whole number only without any remainder")
print("Enter 'quit' to end the program")
user_input = input(": ")

try:
    if user_input == "quit":
        print("You quit")
    elif user_input == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_input == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is " + result)
    elif user_input == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is " + result)
    elif user_input == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is " + result)
    elif user_input == "remainder":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 % num2)
        print("The answer is " + result)
    elif user_input == "exponent":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 ** num2)
        print("The answer is " + result)
    elif user_input == "floor":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 // num2)
        print("The answer is " + result)
    else:
        print("Unknown input")
except:
    print("An error occured")  
