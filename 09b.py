segs = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
pos = {(0,0)}
with open("09.txt") as input:
    for line in input:
        t = line.split()
        for i in range(int(t[1])):
            if t[0] == 'L':
                segs[0][0]-=1
            elif t[0] =='R':
                segs[0][0]+=1
            elif t[0] =='U':
                segs[0][1]+=1
            else:
                segs[0][1]-=1
            for i in range(1,10):
                x = segs[i][0]
                y = segs[i][1]
                if abs(x - segs[i-1][0]) > 1 or abs(y - segs[i-1][1]) > 1 and segs[i-1][0] != segs[i][0]:
                    if segs[i-1][0] > x:
                        segs[i][0]+=1
                    else:
                        segs[i][0]-=1
                if abs(y - segs[i-1][1]) > 1 or abs(x - segs[i-1][0]) > 1 and segs[i-1][1] != segs[i][1]:
                    if segs[i-1][1] > y:
                        segs[i][1]+=1
                    else:
                        segs[i][1]-=1
                if i == 9:
                    pos.add((segs[i][0], segs[i][1]))
print(len(pos))
