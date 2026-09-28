operator.py

print("Arithmetic Operator Calculator")
print("------------------------------")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose an operator:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")
print("%  Modulus")
print("** Power")

operator = input("Enter operator: ")

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        print("Error: Cannot divide by zero.")
        exit()
elif operator == "%":
    if b != 0:
        result = a % b
    else:
        print("Error: Cannot divide by zero.")
        exit()
elif operator == "**":
    result = a ** b
else:
    print("Invalid operator.")
    exit()

print("Result =", result)
