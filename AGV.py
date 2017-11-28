class AGV:
    def __init__(self, prio):
        self.prio = prio
        self.currentPos = 0 #current node
        self.goalPos = 0 #goal node
        self.resPos = [] #list of reserved nodes
        self.prevPos = [] #list of visited nodes, to create the path

    def add_currentPos(self,pos):
        self.currentPos = pos
        return self.currentPos
        

    def add_goalPos(self,pos):
        self.goalPos = pos
        return self.goalPos

    def add_resPos(self,pos):
        del self.resPos[:]
        return self.resPos.append(pos)

    def add_prevPos(self):
        return self.prevPos.append(self.currentPos)





