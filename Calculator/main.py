from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add ,
    "-": subtract ,
    "*": multiply ,
    "/": divide ,
}

want_continue = True
num1 = float(input("Enter the first number: \n"))

# if user wants to perform more than one operation then it stores the previous results
# and let the user tu continue operation of the previous results

while want_continue:
    operation = input("Enter operation: \n")
    num2 = float(input("Enter the second number: \n"))
    result = (operations[operation](num1, num2))
    print("The result is: ", result)

    another = input("Do u want to perform another operation on the lastest output? type 'yes' to continue and 'no' to quit.").lower()
    if another == "no":
        want_continue = False
    if another == "yes":
        num1 = result

