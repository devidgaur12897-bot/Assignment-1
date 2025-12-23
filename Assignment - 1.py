#Task 1-
# Take input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#  mathematical operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

# Display the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate first and last name into full name
full_name = first_name + " " + last_name

# Print greeting

print("hello,", full_name, "welcome to the python program.")