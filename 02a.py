Dict = {"AX": 4,
        "AY": 8,
        "AZ": 3,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 7,
        "CY": 2,
        "CZ": 6,
        }

score = 0

with open("02.txt") as input:
    for line in input:
        s = line.split()
        score += Dict.get(s[0]+s[1])
print(score)
