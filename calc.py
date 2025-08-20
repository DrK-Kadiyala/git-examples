# Simple Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Calculator started!")
result = add(5, 3)
print(f"5 + 3 = {result}")

result = divide(10, 2)
print(f"10 / 2 = {result}")
result = divide(5, 0)
print(f"5 / 0 = {result}")