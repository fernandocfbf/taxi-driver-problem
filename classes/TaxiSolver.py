from turtle import pos
from numpy import true_divide
from State import State
from constants.TaxiSolver import POSSIBILITIES

class TaxiSolver(State):
    def __init__(self,
        operator,
        free,
        taxi_position,
        city_size,
        blocked_positions, 
        passenger_position):
        self.operator = operator
        self.free = free #has passenger?
        self.taxi_position = taxi_position #coordinate pair
        self.city_size = city_size #width and height (w = h)
        self.blocked_positions = blocked_positions #list of coordinate pair
        self.passenger_position = passenger_position #coordinate pair

    def sucessors(self):
        next_nodes = list()
        if (self.near_passenger() and self.free):
            next_nodes.append(TaxiSolver("pickup", False, self.taxi_position, self.size, self.blocked_positions, self.passenger_position))
        for possibility in POSSIBILITIES:
            moviment = POSSIBILITIES[possibility]
            x = self.taxi_position[0] + moviment[0]
            y = self.taxi_position[1] + moviment[1]
            if self.check_valid_position([x, y]) and self.blocked_position([x, y]):
                next_nodes.append(TaxiSolver(possibility, self.free, [x,y], self.size))
        return next_nodes

    def check_valid_position(self, position):
        if (position[0] > 0 and position[0] < self.city_size) and (
            position[1] > 0 and position[1] < self.city_size):
            return True
        return False

    def blocked_position(self, position):
        for blocked_position in self.blocked_positions:
            if blocked_position == position:
                return True
        return False
    
    def near_passenger(self):
        if (self.taxi_position == self.passenger_position):
            return True
        return False

    def description(self):
        return "Taxi driver issue. Takes an passenger and leaves on the destination"
    
    def cost(self):
        return 1 #every moviment has cost equal to one

    def env(self):
        return self.operator #MUST BE UNIQUE - NEED FIX

    def print(self):
        return self.operator

    def h(self):
        return 0