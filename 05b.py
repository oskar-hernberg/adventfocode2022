import re
queueList = []
pileNr = 0
with open("05.txt") as input:
        pileNr = int(len(input.readline())/4)

for x in range(pileNr):
    queueList.append([])
print(queueList)
print(queueList[0])
queueread = False
instrList = []
with open("05.txt") as input:
    for line in input:
        if queueread == True and line.strip():
            t = re.findall(r'\d+', line)   
            instrList.append((list(map(int, list(t)))))
        if queueread == False:
            print(line)
            if line[1] == "1":
                queueread = True
            if queueread == False:
                for i in range(pileNr):
                    char = line[4*i+1]
                    if char != ' ':
                        queueList[i].append(char) 
           #print(line[1*i+1])
print(instrList)
print(queueList)
for instruc in instrList:
    transportList = queueList[instruc[1]-1][0:instruc[0]]
    print(transportList)
  #  queueList[instruc[2]-1].insert(0,queueList[instruc[1]-1].pop(0))
    transportList.reverse()
    for x in range(len(transportList)):
        queueList[instruc[1]-1].pop(0)
        queueList[instruc[2]-1].insert(0,transportList[x])
    print(queueList)
for x in range(pileNr):
    print(queueList[x].pop(0))
