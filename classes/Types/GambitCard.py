class GambitCard:
    def __init__(self):
        self.name = str
        self.description = str
        self.value = int
        self.achieved = False

    def setName(self, name: str):
        self.name = name

    def setDescription(self, description: str):
        self.description = description

    def setValue(self, value: int):
        self.value = value

    def setAchieved(self):
        self.achieved = True

    def getValue(self):
        returnVal: 0
        
        if(self.achieved):
            returnVal = self.value
        
        return returnVal
