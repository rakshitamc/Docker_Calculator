import os

num1 = float(os.getenv("NUM1"))
num2 = float(os.getenv("NUM2"))
operation = os.getenv("OPERATION")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero error"
else:
    result = "Invalid operator"

print(f"Result: {result}")
