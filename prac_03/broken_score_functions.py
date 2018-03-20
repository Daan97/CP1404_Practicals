# """
# CP1404/CP5632 - Practical
# Broken program to determine score status
# """


def main():
    score = float(input("Enter score: "))
    score_message = check_score(score)
    print(score_message)


def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
