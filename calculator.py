# My first calculator program!
# This handles plus, minus, multiply, and divide

print("--- Simple Calculator ---")

# Getting inputs

num1 = float(input("Enter first number: "))
operation = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))


if operation == "+":
    result = num1 + num2
    print("The answer is:", result)

elif operation == "-":
    result = num1 - num2
    print("The answer is:", result)

elif operation == "*":
    result = num1 * num2
    print("The answer is:", result)

elif operation == "/":
    # Basic check  to check for a valid number
    if num2 == 0:
        print("Error! You can't divide by zero.")
    else:
        result = num1 / num2
        print("The answer is:", result)

else:
    print("Invalid operator! Please use +, -, *, or /")

print("Thanks for using my calculator!")
