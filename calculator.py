import os

def calculate(num1, num2, operator):
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    else:
        return "Invalid operator"

if __name__ == "__main__":
    # Fetch values from environment variables
    num1 = os.getenv('NUM1')
    num2 = os.getenv('NUM2')
    operator = os.getenv('OPERATION')

    # Check if all environment variables are set
    if not all([num1, num2, operator]):
        print("Error: Missing environment variables NUM1, NUM2, or OPERATION")
    else:
        result = calculate(num1, num2, operator)
        print(f"Result: {result}")
