
def calc(num1,operation,num2):
    res = 0
    if operation == "+":
        res = num1 + num2
    elif operation == "-":
        res = num1 - num2
    elif operation == "*":
        res = num1 * num2
    elif operation == "/":
        res = num1 / num2
    else:
        res = 0

    return res

def calculator():
    choice = True
    yes_no = "n"
    num1 = 0
    while choice:
        if yes_no == "n":
            num1 = float(input("What's the first number?: \n"))
        print("+\n-\n*\n/")
        operation = input("Pick an operations?: \n")
        num2 = float(input("What's the second number?: \n"))
        val = calc(num1,operation,num2)
        print(f"{num1} {operation} {num2} = {val} ")
        yes_no = input(f"Type 'y' to continue calculating with {val}, or type 'n' to start a new calculation or 'exit' to exit: \n ")
        if yes_no == "y":
            num1 = val
        if yes_no == "exit":
            choice = False

calculator()
