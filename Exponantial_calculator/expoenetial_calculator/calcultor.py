# Mathgaematcial Calculator for exponents.
# This program calculate the exponential values of any given number

# Taking input number from user. 
num = int(input("enter your number:"))

# Displaying menu option.
print("Choose an option:")
print("1.Square Root")
print("2.Cube Root")
print("3.Expontial Value")

# Taking user's choice
Choice = int(input("Enter your choice 1/2/3:"))

# Applying condition for each choosen option.
# Square root Calculation.
if Choice == 1:
    result = num**(0.5)
    print(f"square root of {num} is {result}")

# Cube root Calculation.
elif Choice == 2: 
    result = num**(1/3)
    print(f"Cube root of {num} is {result}")

# Expontial Calculation.
elif Choice == 3:
  Exponent = int(input("Enter exponent"))
  result = num**Exponent
  print (f"Exponential power of{num} is {result}")

# Condition for invalid option.
else : 
    print("invalid option")
    