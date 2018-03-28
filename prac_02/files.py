# Do-from-scratch exercise

# 1.
name = str(input("What is your name: "))
name_text_file = open('name.txt', 'w')
print(name, file=name_text_file)
name_text_file.close()

# 2.
name_text_file = open('name.txt', 'r')
print("Your name is", name)
name_text_file.close()

# 3.
numbers_text_file = open('numbers.txt', 'r')
number1 = int(numbers_text_file.readline())
number2 = int(numbers_text_file.readline())
print("The result is", number1 + number2)
numbers_text_file.close()

# Original attempt
# with open('numbers.txt', 'r') as numbers_text_file:
#     total = 0
#     for line in numbers_text_file:
#         try:
#             total += int(line)
#         except ValueError:
#             pass
# print("The result is ",total)
