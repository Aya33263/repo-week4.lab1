#adding 2 integers
# 1. Displays a welcome message
print("Welcome to the Calculation Program!")

# Function to define and add two integers
def add_numbers():
    # The integers must be defined inside the function as per instructions

    num1 =int (input("enter your first number : "))
    num2 =int (input("enter your second number : "))
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")

# 2. Displays the result by calling the function
add_numbers()