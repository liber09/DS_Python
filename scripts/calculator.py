from typing import Tuple

global OPERATIONS
OPERATIONS = ['+','-','*','/']

#Add function
def add(num1: int, num2: int):
    return num1+num2

#subtract function
def sub(num1: int, num2:int):
    return num1-num2

#Multiplication function
def multi(num1: int, num2: int):
    return num1*num2

#division function
def divide(num1: int, num2:int):
    while num2 == 0:
        print("Can not divide by zero")
        num1,num2 = get_input(prev_value= num1)
        return num1/num2

#Get user input
def get_input(prev_value: int | float | None) -> Tuple[int | float, int]:
    valid = False
    if prev_value:
        valid = True
        validated1 = prev_value
    while not valid: #run as long as value is invalid
        choice1 = input("What is your first number?: ")
        valid = validate_input(choice1.strip())
        if valid:
            validated1 = int(choice1.strip())
    valid = False
    while not valid: #As long as second number is invalid
        choice2 = input("What is your second number?: ")
        valid = validate_input(choice2.strip())
        if valid:
            validated2 = int(choice2.strip())

    return (validated1, validated2)

#Validate input value
def validate_input(choice_string: str) -> bool:
    valid = str.isdigit(choice_string)
    if not valid:
        print("wrong input!!")
    return valid

#What operation does the user want to do
def get_operation() -> str:
    global OPERATIONS
    valid = False
    while not valid:
        operation = input(
            "What kind of calculation do you want to do? ('+', '-', '*' or '/'): ")
        operation = operation.strip()
        if operation in OPERATIONS:
            valid = True
    return operation


def get_continue() -> bool:
    while True:
        choice = input("Do you want to continue? ('y'/'n'): ")
        if choice == "y":
            return True
        if choice == "n":
            print("Thank you and welcome back!")
            return False


#Does the user want to use the answer for another calculation
def get_re_use_result() -> bool:
    while True:
        choice = input("Do you want to reuse the result? ('y'/'n'): ")
        if choice == "y":
            return True
        if choice == "n":
            return False


def main():
    print("Calculator")

    will_continue = True
    result = 0
    reuse = False
    while will_continue:
        if not reuse:
            result = None
        num1, num2 = get_input(prev_value=result)
        operation = get_operation()

        if operation == "+":
            result = add(num1, num2)
        elif operation == '-':
            result = sub(num1, num2)
        elif operation == '*':
            result = multi(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        print(result)

        will_continue = get_continue()
        if not will_continue:
            break
        reuse = get_re_use_result()


main()