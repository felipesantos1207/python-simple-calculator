
# Simple Calculator in Python

print("Welcome to the Calculator!")

print("Choose the operation:")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

option = int(input("Enter the number of the operation: "))

if option == 1:
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    result = value1 + value2
    print("The result of the addition is:", result)

elif option == 2:
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    result = value1 - value2
    print("The result of the subtraction is:", result)

elif option == 3:
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    result = value1 * value2
    print("The result of the multiplication is:", result)

elif option == 4:
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the second number: "))
    if value2 != 0:
        result = value1 / value2
        print("The result of the division is:", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid option. Please choose between 1 and 4.")
