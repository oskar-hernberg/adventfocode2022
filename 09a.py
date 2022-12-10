head = [0,0]
tail = [0,0]
pos = {(0,0)}
with open("09.txt") as input:
    for line in input:
        t = line.split()
        for i in range(int(t[1])):
            if t[0] == 'L':
                head[0]-=1
            elif t[0] =='R':
                head[0]+=1
            elif t[0] =='U':
                head[1]+=1
            else:
                head[1]-=1
            x = tail[0]
            y = tail[1]
            if abs(x - head[0]) > 1 or abs(y - head[1]) > 1 and head[0] != tail[0]:
                if head[0] > x:
                    tail[0]+=1
                else:
                    tail[0]-=1
            if abs(y - head[1]) > 1 or abs(x - head[0]) > 1 and head[1] != tail[1]:
                if head[1] > y:
                    tail[1]+=1
                else:
                    tail[1]-=1
            pos.add((tail[0],tail[1]))
print(len(pos))
