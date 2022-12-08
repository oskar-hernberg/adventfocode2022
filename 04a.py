import re

pairs = 0
with open("04.txt") as input:
    for line in input:
        m = re.findall(r'\d+', line) 
        print(line)
        print(m)
        m[0] = int(m[0])
        m[1] = int(m[1])
        m[2] = int(m[2])
        m[3] = int(m[3])
        if m[0] >= m[2] and m[1] <= m[3]:
            print("+1 1")
            pairs+=1
        elif m[0] <= m[2] and m[1] >= m[3]:
            print("+1 2")
            pairs+=1
        print(pairs)
        print("\n\n")
print(pairs)
