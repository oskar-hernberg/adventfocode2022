highestCount = 0
currentCount = 0
with open("01.txt") as input:
    for line in input:
        if line.strip() == "": 
            if highestCount < currentCount:
                highestCount = currentCount
            currentCount = 0
        else:   
            currentCount += int(line)
print(highestCount)

