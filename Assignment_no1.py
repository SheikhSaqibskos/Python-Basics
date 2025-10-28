# Assignment_no_1: Basic Calculator
# Prepared By: Sheikh Saqib
# Description: Basic calculator that performs +, -, *, / with error handling.

def calculator():
    print("=== Basic Python Calculator ===")
    
    try:
        # Taking input
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operator! Please use +, -, *, or /")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid number input! Please enter numeric values only.")
    except Exception as e:
        print(f"Unexpected error: {e}")

calculator()
