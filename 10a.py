count = []
cycle = 1
regx = 1
with open("10.txt") as input:
    for line in input:
        c = line.split()
        if c[0] == "noop":
            if cycle == 20 or cycle % 40 == 20:
                count.append(regx*cycle)
                print(regx)
                print(cycle)
                print(regx*cycle)
                print("\n")
            cycle+=1
        else:
            for i in range(2):
                if cycle == 20 or cycle % 40 == 20:
                    print(regx)
                    print(cycle)
                    print(regx*cycle)
                    print("\n")
                    count.append(regx*cycle)
                cycle+=1
            regx +=int(c[1])

print(sum(count))
