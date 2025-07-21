# Basic Arithmetic Calculator

# Get numbers from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b if b != 0 else 'Cannot divide by zero'}")
