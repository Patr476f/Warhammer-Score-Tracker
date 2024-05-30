import DeploymentCard
import PrimaryMissionCard
import MissionRuleCard
import SecondaryMissionCard
import GambitCard

class MissionDeck:
    def __init__(self, name):
        self.name = name
        self.deployments = []
        self.primaries = []
        self.missionRules = []
        self.secondaries = []
        self.gambits = []

    def addDeploymentCard(self, deployment):
        if(isinstance(deployment, DeploymentCard)):
            self.deployments.append(deployment)
        else:
            return TypeError("Couldn't add primary card, not correct type!")
    
    def addPrimaryCard(self, primary):
        if(isinstance(primary, PrimaryMissionCard)):
            self.primaries.append(primary)
        else:
            return TypeError("Couldn't add primary card, not correct type!")
        
    def addMissionRuleCard(self, missionRule):
        if(isinstance(missionRule, MissionRuleCard)):
            self.missionRules.append(missionRule)
        else:
            return TypeError("Couldn't add primary card, not correct type!")

    def addSecondaryCard(self, secondary):
        if(isinstance(secondary, SecondaryMissionCard)):
            self.secondaries.append(secondary)
        else:
            return TypeError("Couldn't add primary card, not correct type!")
    
    def addGambitCard(self, gambit):
        if(isinstance(gambit, GambitCard)):
            self.gambits.append(gambit)
        else:
            return TypeError("Couldn't add primary card, not correct type!")
    
    def getDeploymentCards(self):
        return self.deployments
    
    def getMissionRuleCards(self):
        return self.primaries   
     
    def getPrimaryCards(self):
        return self.missionRules    
    
    def getSecondaryCards(self):
        return self.secondaries    

    def getGambitCards(self):
        return self.gambits