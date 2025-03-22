def add(x, y):
    # Function to add two numbers
    return x + y

def subtract(x, y):
    # Function to subtract two numbers
    return x - y

def multiply(x, y):
    # Function to multiply two numbers
    return x * y

def divide(x, y):
    # Function to divide two numbers, checking for division by zero
    if y == 0:
        return "Error! Division by zero."
    return x / y

def floor_divide(x, y):
    # Function to perform floor division, checking for division by zero
    if y == 0:
        return "Error! Division by zero."
    return x // y  

def modulus(x, y):
    # Function to find the modulus (remainder), checking for division by zero
    if y == 0:
        return "Error! Division by zero."
    return x % y 

# Display the available operations
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Modulus")

# Get user choice of operation
choice = input("Enter choice (1/2/3/4/5/6): ")

# Check if the choice is valid
if choice in ('1', '2', '3', '4', '5', '6'):
    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation and display the result
    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        print(f"Result: {floor_divide(num1, num2)}")
    elif choice == '6':
        print(f"Result: {modulus(num1, num2)}")
else:
    # Handle invalid input
    print("Invalid input! Please enter a valid choice.")

