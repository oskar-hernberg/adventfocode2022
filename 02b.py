Dict = {"AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7,
        }

score = 0

with open("02.txt") as input:
    for line in input:
        s = line.split()
        score += Dict.get(s[0]+s[1])
print(score)
