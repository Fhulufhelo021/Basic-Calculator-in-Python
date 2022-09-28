#A a menu for player to choose

print("Select a operation to choose")

print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divison")

operation = input()

print("Run operation")

if operation == "1":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your 2nd number: ")
    print("The sum of the two digits is: " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your 2nd number: ")
    print("The sum of the two digits is: " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your 2nd number: ")
    print("The sum of the two digits is: " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter your first number: ")
    num2 = input("Enter your 2nd number: ")
    print("The sum of the two digits is: " + str(int(num1) // int(num2)))
else:
    print("Invail operation has been entered")
