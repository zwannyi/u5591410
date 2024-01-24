def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Can't divide by zero"
    else:
        return num1 / num2
    
def calculator():
    print("Select Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input()

    if choice == "1":
        num1 = int(input("Enter number: "))
        num2 = int(input("Enter number: "))
        print(add(num1, num2))

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            print(f"Result: {result}\n")
                
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

calculator()