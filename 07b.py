smolsize = 0

class Node:
    def __init__(self):
        self.nodes = []
        self.dir = False
        self.size = 0
        self.name = ""
        self.parent = None
def sizeidentifier():
    rootNode = None
    with open("06.txt") as input:
        currentNode = None
        for line in input:
            if line.startswith("$") == True:
                if line.startswith("$ cd ..") == True:
                    currentNode = currentNode.parent
                elif line.startswith("$ cd") == True:
                    n = Node()
                    n.nodes = set()
                    n.dir = True
                    n.name = line.split()[2]
                    n.parent = currentNode
                    if rootNode != None:
                        n.parent.nodes.add(n)
                    currentNode = n
                    if rootNode == None:
                        rootNode = currentNode
            elif line.startswith("dir"):
                n = Node()
            else:
                currentNode.size+=int(line.split()[0])

    recur(rootNode)
    smallestPos = 70000000-rootNode.size
    smallestPos = 30000000-smallestPos
    print(rootNode.size)
    list.sort(nodesizes)
    print(smallestPos)
    print(nodesizes)
    for i in nodesizes:
        if i >= smallestPos:
            print(i)
            break
        

def findsmol(node):
    for n in node.nodes:
        recur(n)
    if node.size <= 100000:
        x.append(node.size)
    return node.size


x = []
nodesizes = []
def recur(node):
    for n in node.nodes:
        node.size+=recur(n)
    if node.size <= 100000:
        x.append(node.size)
    nodesizes.append(node.size)
    return node.size

if __name__ == "__main__":
   sizeidentifier() 
   print(sum(x))
