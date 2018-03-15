"""Daan Felton-Busch"""


def main():
    name = get_name()
    print_name(name)


def print_name(name, frequency=2):
    print(name[::frequency])


def get_name():
    name = str(input("Enter your name: "))
    while name == "":
        print("Invalid name!")
        name = str(input("Enter your name: "))
    return name


main()
