def checkvisible(x,y):
    n = treemap[x][y]
    return cvn(x,y,n) or cvs(x,y,n) or cvw(x,y,n) or cve(x,y,n)
    
def cvn(x,y,n):
    if x <= 0:
        return True
    if treemap[x-1][y] >= n:
        return False
    return cvn(x-1,y,n)

def cvs(x,y,n):
    if x >= len(treemap)-1:
        return True
    if treemap[x+1][y] >= n:
        return False
    return cvs(x+1,y,n)

def cvw(x,y,n):
    if y <= 0:
        return True
    if treemap[x][y-1] >= n:
        return False
    return cvw(x,y-1,n)

def cve(x,y,n):
    if y >= len(treemap[x])-1:
        return True
    if treemap[x][y+1] >= n:
        return False
    return cve(x,y+1,n)

treemap = []
visibletrees = 0 

with open("08.txt") as input:
    for line in input:
        treemap.append(list(map(int,line.strip())))

for x in range(len(treemap)):
    for y in range(len(treemap[x])):
        if checkvisible(x,y) == True:
            #print(x)
            #print(y)
            #print(treemap[x][y])
            #print("\n")
            visibletrees+=1

print(treemap)
print(visibletrees)


