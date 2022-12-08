import re

pairs = 0
with open("04.txt") as input:
    for line in input:
        m = re.findall(r'\d+', line) 
        m[0] = int(m[0])
        m[1] = int(m[1])
        m[2] = int(m[2])
        m[3] = int(m[3])
        if m[0] <= m[3] and m[0] >= m[2] or m[1] >= m[2] and m[1] <= m[3]:
            pairs+=1
        elif m[2] <= m[1] and m[2] >= m[0] or m[3] >= m[0] and m[3] <= m[1]:
            pairs+=1
print(pairs)
