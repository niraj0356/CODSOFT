
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation: +, -, *, /")
    operation = input("Enter operation: ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    else:
        return "Invalid operation!"
    
    return f"Result: {result}"

print(calculator())
