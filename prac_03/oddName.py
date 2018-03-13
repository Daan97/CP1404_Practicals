"""Daan Felton-Busch"""
name = str(input("Enter your name: "))
while name == "":
    print("Invalid name!")
    name = str(input("Enter your name: "))
print(name[0::2])