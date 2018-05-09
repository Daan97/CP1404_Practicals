"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
    else:
        print("Invalid short state")
    state = input("Enter short state: ").upper()

for state in STATE_NAMES:
    print("{0} is {1}".format(state, STATE_NAMES[state]))


COLOUR_CODES = {"ALICEBLUE": "#f0f8ff", "ANTIQUEWHITE": "#faebd7", "ANTIQUEWHITE1": "#ffefdb",
                "ANTIQUEWHITE2": "#eedfcc", "ANTIQUEWHITE3": "#cdc0b0", "ANTIQUEWHITE4": "#8b8378",
                "AQUAMARINE1": "#7fffd4", "AQUAMARINE2": "#76eec6", "AQUAMARINE4": "#458b74", "AZURE1": "#f0ffff"}

for colour in COLOUR_CODES:
    print("{0} is {1}".format(colour, COLOUR_CODES[colour]))
colour = input("Enter a colour: ").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").upper()
