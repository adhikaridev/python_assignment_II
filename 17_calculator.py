# 17. Write a program that serves as a basic calculator. It asks for two
# numbers, then it asks for an operator. Gracefully deal with input that
# doesn't cleanly convert to numbers. Deal with division by zero errors.

try:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
except Exception as e:
    exit("Invalid input. Please enter number.")
op = input("Enter an operator: ")

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    try:
        result = n1 / n2
    except Exception as e:
        exit("Cannot divide by zero.")
else:
    exit("Invalid operator. Please enter one of the four basic operators.")
print("Result: ", result)
