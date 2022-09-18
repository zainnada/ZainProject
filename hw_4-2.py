# Homework4 Q2
import math

my_id = 0
my_premesion = False
num1 = input("Enter the first number: ")
condition1 = num1.isdigit() or num1.__contains__(".")

if condition1:
    op = input("Choose The Operator\n1_+\n2_-\n3_*\n4_/\n5_^\n6_%\n")
    my_premesion = True
    if op == "1" or op == "+":
        my_id = 1
    elif op == "2" or op == "-":
        my_id = 2
    elif op == "3" or op == "*":
        my_id = 3
    elif op == "4" or op == "/":
        my_id = 4
    elif op == "5" or op == "^":
        my_id = 5
    elif op == "6" or op == "%":
        my_id = 6
    else:
        my_premesion = False
        print("Error..")

else:
    print("Error")
if my_premesion:
    num2 = input("Enter the second number: ")
    condition2 = num2.isdigit() or num2.__contains__(".")
    if condition2:
        if my_id == 1:
            result = float(num1) + float(num2)
        elif my_id == 2:
            result = float(num1) - float(num2)
        elif my_id == 3:
            result = float(num1) * float(num2)
        elif my_id == 4:
            result = float(num1) / float(num2)
        elif my_id == 5:
            result = float(num1) ** float(num2)
        elif my_id == 6:
            result = float(num1) % float(num2)
        print(result)
        ex_op = input("Extra choices:\n1_Print a rounded of the number\n2_print without a decimal point\n3_Exit\n")
        if ex_op == "1":
            result = round(result)
            print(result)
        elif ex_op == "2":
            result = math.floor(result)
            print(result)
        elif ex_op == "3":
            print("Exit")
        else:
            print("Error")
    else:
        print("Error")

# Done
