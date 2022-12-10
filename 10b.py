class Crt:
    def __init__(self):
        self.rows = [['.'] * 40] * 6
        self.drawbuffer = list('.' * 240)
        self.cycle = 1
        self.regx = 1
    def executeCommands(self):
        with open("10.txt") as input:
            for line in input:
                c = line.split()
                row = int((self.cycle-1)/40)
                if c[0] == "noop":
                    self.draw(row)
                    self.cycle+=1
                else:
                    for i in range(2):
                        self.draw(row)
                        self.cycle+=1
                    self.regx +=int(c[1])
    def draw(self, row):
        drawpos = self.cycle-1
        print(self.regx)
        print(drawpos)
        print("\n")
        if abs(self.regx - drawpos %40) <= 1:
            self.drawbuffer[drawpos] = "#"
    def __str__(self):
 #       return "hello"
        crtstr = ""
        for i in range(0, len(self.drawbuffer), 40):
            d = self.drawbuffer[i:i+40]
            crtstr+=''.join(d)    
            crtstr+='\n'
        return crtstr
if __name__ == "__main__":
    crt = Crt()
    crt.executeCommands()
    print(crt)
