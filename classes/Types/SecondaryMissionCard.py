class SecondaryMissionRule:
    def __init__(self):
        self.description = None
        self.fixedValue = None
        self.tacticalValue = None

    def setDescription(self, description:str ):
        self.description = description
    def setFixed(self, value: int):
        self.fixedValue = value
    def setTactical(self, value: int):
        self.tacticalValue = value

class SecondaryMissionCard:
    def __init__(self):
        self.name = None
        self.limit = None
        self.rules = []
        self.fixed = False

    def setName(self, name: str):
        self.name = name
    def setLimit(self, limit: int):
        self.limit = limit
    def addRule(self, rule):
        if(isinstance(rule, SecondaryMissionRule)):
            self.rules.append(rule)
        else:
            return TypeError("Couldn't add secondary rule, wrong type")
    def setFixed(self, fixed):
        self.fixed = fixed