def checkvisible(x,y):
    n = treemap[x][y]
    return cvn(x,y,n,0) * cvs(x,y,n,0) * cvw(x,y,n,0) * cve(x,y,n,0)
    
def cvn(x,y,n,d):
    if x <= 0:
        return d
    if treemap[x-1][y] >= n:
        return d+1
    return cvn(x-1,y,n,d+1)

def cvs(x,y,n,d):
    if x >= len(treemap)-1:
        return d
    if treemap[x+1][y] >= n:
        return d+1
    return cvs(x+1,y,n, d+1)

def cvw(x,y,n,d):
    if y <= 0:
        return d
    if treemap[x][y-1] >= n:
        return d+1
    return cvw(x,y-1,n, d+1)

def cve(x,y,n,d):
    if y >= len(treemap[x])-1:
        return d
    if treemap[x][y+1] >= n:
        return d+1
    return cve(x,y+1,n, d+1)

treemap = []
with open("08.txt") as input:
    for line in input:
        treemap.append(list(map(int,line.strip())))
maxr = []
for x in range(len(treemap)):
    for y in range(len(treemap[x])):
        maxr.append(checkvisible(x,y))
print(max(maxr))


