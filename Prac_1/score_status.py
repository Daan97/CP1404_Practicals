# """
# CP1404/CP5632 - Practical
# Broken program to determine score status
# """
#
# # TODO: Fix this!

score = float(input("Enter score: "))

if score >= 90 and score < 100:
    print("Excellent score")
elif score > 100:
    print("Invalid Score")
elif score >= 50:
    print("Passable")
elif score < 50 and score > 0:
    print("Bad")
else:
    print("Invalid score")


#   Solution
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")