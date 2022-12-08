chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

with open("03.txt") as input:
    backpack = input.read().split()
    for line in backpack:
        s = set()
        arr = list(line)
        for i in range(0, int(len(arr)/2)):
            for j in range(int(len(arr)/2), len(arr)):
                if arr[i] == arr[j]:
                    s.add(arr[i])
        for dup in s:
            sum+= chars.index(dup)+1
            
print(sum)

