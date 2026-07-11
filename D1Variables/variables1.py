# Day 1 Variables
#Asked to write name,age,college name,fav Programming Lang,and to print them and their type
# My Way:

name="Devshree"
age=20
clg="G H Raisoni International Skill Tech University"
prog="Python"

print(name)
print(type(name))

print(age)
print(type(age))

print(clg)
print(type(clg))

print(prog)
print(type(prog))
print()

# IMPROVEMENTS
print("Name:",name)
print("Type:", type(name))

print(f"Name: {name}")
print(f"Type: {type(name)}")

#Cleaner way
print(f"Name:{name} \nType:{type(name).__name__}")


"""Challenge 
Write a program that:
Name: Devshree
Age: 20

After 5 years, I will be 25 years old.

Rules:
Use variables.
Don't directly write 25 in the print() statement.
Calculate it using the age variable."""

print(f"Name:{name}")
print(f"Age:{age}")
print(f"After 5 years I will be {age+5} years old")

name = "Devshree"
a = 7
print(f"{name.upper()} has {len(name)} letters.")

print(f"{name.capitalize()} is {len(name)} letters long and {a} squared is {a**2}.")
