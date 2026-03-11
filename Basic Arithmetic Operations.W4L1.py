# Basic Arithmetic Operations
def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def add_and_multiply(num1, num2, num3): 

    #add process

    sum_val = add(num1, num2)
    
    #multiply process
    result = multiply(sum_val, num3)
    
    return result

# this part for user 

print(" HELLO Enter three numbers to add the first two, then multiply by the third.\n")

# enter the numbers

a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
c = float(input("Enter third number (c): "))

# call the function 
final_result = add_and_multiply(a, b, c)

# for the result
print(final_result)
