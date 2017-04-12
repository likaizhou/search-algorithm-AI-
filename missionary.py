### File: missionary.py
### Implements the missionaries and cannibals problem for state
### space search

from search import *

class MissionaryState():
    """
    In the missionaries and cannibals problem, three missionaries and three cannibals 
    must cross a river using a boat which can carry at most two people, under 
    the constraint that, for both banks, if there are missionaries present on the bank, 
    they cannot be outnumbered by cannibals (if they were, the cannibals would eat 
    the missionaries). The boat cannot cross the river by itself with no people on board.
    """
    def __init__(self, missionary, cannibal, boat):
        self.missionary = missionary
        self.cannibal = cannibal
        self.boat = boat
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "("+str(self.missionary)+","+str(self.cannibal)+","+str(self.boat)+")"
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if self.missionary < 0 or self.cannibal < 0: return 1
        if self.missionary > 3 or self.cannibal > 3: return 1
        if self.missionary != 0 and self.missionary < self.cannibal: return 1
        if self.missionary != 3 and 3 - self.missionary < 3 - self.cannibal: return 1
        if self.boat < 0 or self.boat > 1: return 1
        return 0
    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.missionary==state.missionary and self.cannibal==state.cannibal and self.boat ==state.boat
    def L01(self):    
        return MissionaryState(self.missionary, self.cannibal - 1, self.boat - 1)
    def L10(self):    
        return MissionaryState(self.missionary - 1, self.cannibal, self.boat - 1) 
    def L11(self):    
        return MissionaryState(self.missionary - 1, self.cannibal + 1, self.boat - 1)
    def L02(self):    
        return MissionaryState(self.missionary, self.cannibal - 2, self.boat - 1)
    def L20(self):    
        return MissionaryState(self.missionary - 2, self.cannibal, self.boat - 1)
    def R01(self):    
        return MissionaryState(self.missionary, self.cannibal + 1, self.boat + 1)
    def R10(self):    
        return MissionaryState(self.missionary + 1, self.cannibal, self.boat + 1) 
    def R11(self):    
        return MissionaryState(self.missionary + 1, self.cannibal + 1, self.boat + 1)
    def R02(self):    
        return MissionaryState(self.missionary, self.cannibal + 2, self.boat + 1)
    def R20(self):    
        return MissionaryState(self.missionary + 2, self.cannibal, self.boat + 1)
    def operatorNames(self):    
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["L01", "L10","L11","L02","L20",
                "R01", "R10","R11","R02","R20"]
    def applyOperators(self):  
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.
        """
        return [self.L01(), self.L10(), self.L11(), self.L02(), self.L20(),
                self.R01(), self.R10(), self.R11(), self.R02(), self.R20()]
Search(MissionaryState(3,3,1), MissionaryState(0,0,0))