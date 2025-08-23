def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

if _name_ == "_main_":
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    choice = input("Enter choice: ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '+':
        print(f"Result: {add(num1, num2)}")
    elif choice == '-':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '*':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '/':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Input")
