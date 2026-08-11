print("Welcome to my python program")
print("==============================")
print("This program collects your basic information")
print("And Display your details, data types and memory addresses")
print()

#collect information
name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height in cm: "))
favourite_number=int(input("Enter your favourite number: "))
print()

#Data processing
birth_year=2026-age

#Display values, data types and memory addresses
print("Data Information")
print("Name: ", name)
print("Data type: ", type(name))
print("Memory address: ",id(name))
print()

print("Age: ", age)
print("Data type: ", type(age))
print("Memory address: ",id(age))
print()

print("Height: ", height)
print("Data type: ", type(height))
print("Memory address: ",id(height))
print()

print("Favourite Number: ", name)
print("Data type: ", type(favourite_number))
print("Memory address: ",id(favourite_number))
print()

#Display result
print("User Information")
print("====================")
print("Name:", name)
print("Age:",age,"years")
print("Height:",height,"cm")
print("favourite number:",favourite_number)
print("Approximate Birth Yeaar:", birth_year)
print()

#Type conversion
print("Type conversion")
print("Age was converted from string to integer using int().")
print("Height was converted from string to float using float().")
print("Favourite number was converted from string to interger using int()")
print()

#Exit message

print("Thank you for using this program")
