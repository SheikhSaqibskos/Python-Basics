# OOP Calculator using Abstract Classes and Inheritance
# Author: Sheikh Saqib
# Description: Demonstrates inheritance and abstract methods in a calculator.

from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def calculate(self, a, b):
        """Perform calculation and return the result"""
        pass


class Add(Operation):
    def calculate(self, a, b):
        return a + b

class Subtract(Operation):
    def calculate(self, a, b):
        return a - b

class Multiply(Operation):
    def calculate(self, a, b):
        return a * b

class Divide(Operation):
    def calculate(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed!")
        return a / b

class Calculator:
    def __init__(self):
        print("=== OOP Python Calculator ===")

    def perform_operation(self):
        try:
            a = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()
            b = float(input("Enter second number: "))

            operations = {
                '+': Add(),
                '-': Subtract(),
                '*': Multiply(),
                '/': Divide()
            }
            if operator in operations:
                operation = operations[operator]
                result = operation.calculate(a, b)
                print(f"Result: {a} {operator} {b} = {result}")
            else:
                print("Error: Invalid operator! Please use +, -, *, or /")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
if __name__ == "__main__":
    calc = Calculator()
    calc.perform_operation()
