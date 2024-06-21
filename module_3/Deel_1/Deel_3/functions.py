# functions.py

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        return "Error: Division by zero is undefined"
    return number1 / number2
