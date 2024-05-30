class PrimaryMissionRule:
    def __init__(self):
        self.description = None
        self.value = None
        self.limit = None
        self.bonusDescription = None
        self.extraPoints = []
    
    def setDescription(self, description: str):
        self.description = description

#used to give extra description for last battle round
    def addBonusDescription(self, bonus: str):
        self.bonusDescription = bonus  

#used for missions that give additional points when certain criterias are met
    def addExtraPoints(self, extraDescription: str, extraValue: int):
        extraPoint = {"description": extraDescription, "value": extraValue, "achieved": False}
        self.extraPoints.append(extraPoint)

    def getExtraPoints(self):
        return self.extraPoints
    
    def setExtraPointAchieved(self, index: int):
        if 0 <= index < len(self.extraPoints):
            self.extraPoints[index]["achieved"] = True
        else:
            print(f"Index {index} is out of range")

    def givePoints(self, amount: int):
        points = self.value*amount

        for extra in self.extraPoints:
            if(extra.get("achieved")):
                points += extra.get("value")
        
        if(points > self.limit):
            points = self.limit

        return points

class PrimaryMissionCard:
    def __init__(self):
        self.battleRoundRule = None
        self.specialRule = None
        self.endOfBattleRule = None
        self.name = ""

    def addBattleRoundRule(self, rule):
        if(isinstance(rule, PrimaryMissionRule)):
            self.battleRoundRule = rule
        else:
            return TypeError("Couldn't add primary rule, not correct type!")

    def addSpecialRule(self, rule):
        if(isinstance(rule, PrimaryMissionRule)):
            self.specialRule = rule
        else:
            return TypeError("Couldn't add primary special rule, not correct type!")

    def addEndOfBattleRule(self, rule):
        if(isinstance(rule, PrimaryMissionRule)):
            self.endOfBattleRule = rule
        else:
            return TypeError("Couldn't add primary end of battle rule, not correct type!")

    def setName(self, name: str):
        self.name = name