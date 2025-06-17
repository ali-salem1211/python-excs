# Define calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero"

# Example usage
print("Add: ", add(10, 5))        # 15
print("Subtract: ", subtract(10, 5))  # 5
print("Multiply: ", multiply(10, 5))  # 50
print("Divide: ", divide(10, 5))      # 2.0
