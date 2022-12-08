chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

with open("03.txt") as input:
    backpacks = input.read().split()
    grouped = []
    for index in range(0, len(backpacks), 3):
        grouped.append(backpacks[index : index+3])
    for group in grouped:
        s = set()
        for a in group[0]:
            for b in group[1]:
                for c in group[2]:
                    if a == b ==c:
                        s.add(a)
        for dup in s:
            sum+= chars.index(dup)+1
print(sum)

