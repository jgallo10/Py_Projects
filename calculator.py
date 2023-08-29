# creating a regular calcualtor

def add(n1, n2):
    total = n1 + n2
    return total
    
def subtract(n1, n2):
    total = n1 - n2
    return total
    
def multiply(n1, n2):
    total = n1 * n2
    return total
    
def divide(n1, n2):
    total = n1 / n2
    return total

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = int(input("What is the first number?: \n"))
    
    
        
    continueing = True
    
    while continueing:
        for operator in operations:
            print(operator)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("what is the second number?: \n"))
        
        calculation = operations[operation_symbol]
        total = calculation(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {total} \n")
        
        if input(f"Type 'y' to continue calcualting with {total}, or type 'n' to start a new calulation: ") == "y":
            num1 = total
        else:
            continueing = False
            calculator()

calculator()