class Node:
    def __init__(self):
        self.nodes = []
        self.dir = False
        self.size = 0
        self.name = ""
        self.parent = None
def sizeidentifier():
    totalCount = 0
    rootNode = None
    with open("06.txt") as input:
        currentNode = None
        for line in input:
            if line.startswith("$") == True:
                if line.startswith("$ cd ..") == True:
#                    currentNode.parent.size+= currentNode.size
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
               # n.dir = True
                #n.name = line.split()[1]
                #n.parent = currentNode
                #n.parent.nodes.add(n)
            else:
                currentNode.size+=int(line.split()[0])
                #n = Node()
                #n.size = int(line.split()[0])
                #n.name = line.split()[1]
                #n.parent = currentNode
                #count+= n.size 
            print(currentNode.name)
            print(currentNode.nodes)


    print("here") 
    recur(rootNode)

x = []
def recur(node):
    #if len(node.nodes) == 0:
     #       return
    
    for n in node.nodes:
        node.size+=recur(n)
    if node.size <= 100000:
        x.append(node.size)
    return node.size

if __name__ == "__main__":
   sizeidentifier() 
   print(sum(x))
