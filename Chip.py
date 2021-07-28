class Chip:
    state = ""
    def __init__(self,state):
        self.state = state

    def getState(self):
        return self.state

    
    def setState(self,state):
        self.state = state

    def __str__(self):
        return state
    