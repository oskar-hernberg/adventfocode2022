highestValueArr = [0]
index = 0
with open("01.txt") as input:
    for line in input:
        if line.strip() == "": 
            index += 1
            highestValueArr.append(0)
        else:   
            highestValueArr[index] += int(line)
highestValueArr.sort(reverse=True)
print(sum(highestValueArr[:3]))

