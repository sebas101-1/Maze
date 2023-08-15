import sys
class Maze():
    def __init__(self, file):
        self.width = len(file[0].strip())  # Strip newline characters
        self.height = len(file)
        self.Mazel = []
        self.Frontier = []
        self.blacklist = []
        self.finished = False
        self.numExplored = 0
        for i in range(self.height):
            self.Mazel.append([""])
            for x in range(self.width):
                self.Mazel[i][0] += file[i][x]
                if(file[i][x] == "B"):
                    self.End = (x,i)
                elif(file[i][x] == "A"):
                    self.Start = (x,i)
                    self.Frontier.append(Node(self.Start,None,None))
                    print("Start")


            
    def printMaze(self):
        for b in range(len(self.Mazel)):
            print(self.Mazel[b][0])  # Access the first (and only) element of each sublist
    def Solve(self):
        print("Solving")
        while(self.finished == False):
            self.numExplored += 1
            self.remove()

    def remove(self):
        removed = self.Frontier[0]
        del self.Frontier[0]
        self.blacklist.append(removed)
        if(removed.state == self.End):
            print("finished")
            print("number explored "+str(self.numExplored))
            self.trace(removed)
            self.finished = True
        else:
            if(removed.state[0] != self.width-1 and self.Mazel[removed.state[1]][0][removed.state[0]+1] != "#" and self.inBlack((removed.state[0]+1,removed.state[1])) == False):
                self.Frontier.append(Node((removed.state[0]+1,removed.state[1]),(0,1),removed))
            if(removed.state[0] != 0 and self.Mazel[removed.state[1]][0][removed.state[0]-1] != "#" and self.inBlack((removed.state[0]-1,removed.state[1])) == False):
                self.Frontier.append(Node((removed.state[0]-1,removed.state[1]),(0,1),removed))
            if(removed.state[1] != 0 and self.Mazel[removed.state[1]-1][0][removed.state[0]] != "#" and self.inBlack((removed.state[0],removed.state[1]-1)) == False):
                self.Frontier.append(Node((removed.state[0],removed.state[1]-1),(0,1),removed))
            if(removed.state[1] < self.height-1 and self.Mazel[removed.state[1]+1][0][removed.state[0]] != "#" and self.inBlack((removed.state[0],removed.state[1]+1)) == False):
                self.Frontier.append(Node((removed.state[0],removed.state[1]+1),(0,1),removed))
    def inBlack(self, node):
        for lol in range(len(self.blacklist)):
            if(node == self.blacklist[lol].state):
                return True
        return False
    def trace(self, fin):
        while fin.state != self.Start:
            fin = fin.parent
            
            # Modify the string in self.Mazel by replacing a character with "X"
            if(fin.state != self.Start):
                row = self.Mazel[fin.state[1]][0]
                updated_row = row[:fin.state[0]] + "*" + row[fin.state[0] + 1:]
                self.Mazel[fin.state[1]][0] = updated_row


class Node():
    def __init__(self, state, action, parent):
        self.parent = parent
        self.action = action
        self.state = state

with open("maze3.txt") as f:
    contents = f.readlines()
u = "up"
d = "down"
l = "left"
r = "right"
m = Maze(contents)
m.printMaze()
m.Solve()
m.printMaze()


