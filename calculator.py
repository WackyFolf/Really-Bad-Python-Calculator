numberOne = float(input("What is the first number?\n"))
numberTwo = float(input("What is the second number?\n"))
operator = (input("What is the operator? (Options: * / + -)\n"))

def subtract(numOne, numTwo):
    return numOne-numTwo
def add(numOne, numTwo):
    return numOne+numTwo
def multiply(numOne, numTwo):
    return numOne*numTwo
def divide(numOne, numTwo):
    return numOne/numTwo
if operator is ("*"):
    result = (multiply(numberOne, numberTwo))
if operator is ("/"):
    if (numberTwo==0):
        result = ("Error. Cannot divide by 0. Please run the program again, and try not to be stupid.")
    else:
        result = (divide(numberOne, numberTwo))
if operator is ("+"):
    result = (add(numberOne, numberTwo))
if operator is ("-"):
    result = (subtract(numberOne,numberTwo))
if operator is not ("+" or "-" or "*" or "/"):
    result=("That isn't an operator. Please run the program again, and try not to be stupid.")
print("\n")
print(result)
print("\n")