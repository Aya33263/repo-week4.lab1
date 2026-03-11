# Basic Arithmetic Operations
def add (a, b):
    return a+b

def multiply (x,c):
    return x*c

def add_and_multiply (a, b, c):
    sum_result =add (a, b)  #calling the add function

    # Making it flexible with input()
    # Note: input() always returns text, so we use float() to convert it to a number
    #print("Enter three numbers to add the first two, then multiply by the third.")

    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    c = float(input("Enter third number (c): "))
    product_result = multiply (sum_result, c)  #calling the multiply function
    return product_result

    print(result )  