from State import State

class TaxiSolver(State):
    def __init__(self, operator):
        self.operator = operator

    def description(self):
        return "Taxi driver issue. Takes an passenger and leaves on the destination"
    
    def cost(self):
        return 1 #every moviment has cost equal to one

    def print(self):
        return self.operator

    def h(self):
        return 0