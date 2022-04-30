from classes.State import State

from utils.GetBlockedPositions import getBlockedPositions

class TaxiSolver(State):
    def __init__(self,
        operator,
        free,
        taxi_position,
        city_size,
        blocked_positions, 
        passenger_position,
        destination):
        self.operator = operator
        self.free = free #has passenger?
        self.taxi_position = taxi_position #coordinate pair
        self.city_size = city_size #width and height
        self.blocked_positions = getBlockedPositions(blocked_positions) #list of coordinate pair
        self.passenger_position = passenger_position #coordinate pair
        self.destination = destination #coordinate pair

    def sucessors(self):
        next_nodes = list()
        up = (self.taxi_position[0] - 1, self.taxi_position[1])
        down = (self.taxi_position[0] + 1, self.taxi_position[1])
        left = (self.taxi_position[0], self.taxi_position[1] - 1)
        right = (self.taxi_position[0], self.taxi_position[1] + 1)

        if not(self.blocked_position(up)):
            next_nodes.append(TaxiSolver("up", self.free, up, self.city_size, self.blocked_positions, self.passenger_position, self.destination))
        if not(self.blocked_position(down)):
            next_nodes.append(TaxiSolver("down", self.free, down, self.city_size, self.blocked_positions, self.passenger_position, self.destination))
        if not(self.blocked_position(left)):
            next_nodes.append(TaxiSolver("left", self.free, left, self.city_size, self.blocked_positions, self.passenger_position, self.destination))
        if not(self.blocked_position(right)):
            next_nodes.append(TaxiSolver("right", self.free, right, self.city_size, self.blocked_positions, self.passenger_position, self.destination))
        if self.near_passenger():
            next_nodes.append(TaxiSolver("pickup", False, self.taxi_position, self.city_size, self.blocked_positions, self.passenger_position, self.destination))
        
        return next_nodes

    def blocked_position(self, position):
        for blocked_position in self.blocked_positions:
            if blocked_position[0] == position[0] and blocked_position[1] == position[1]:
                return True
        return False
    
    def near_passenger(self):
        if (self.taxi_position[0] == self.passenger_position[0] and (
            self.taxi_position[1] == self.passenger_position[1]
        )):
            return True
        return False

    def is_goal(self):
        return self.taxi_position[0] == self.destination[0] and (self.taxi_position[1] == self.destination[1]) and not(self.free)

    def description(self):
        return "Taxi driver issue. Takes an passenger and leaves on the destination"
    
    def cost(self):
        return 1 #every moviment has cost equal to one

    def env(self):
        return ";" + str(self.operator) + ";" + str(self.taxi_position) + ";" + str(self.free) + ";" + str(self.passenger_position)

    def print(self):
        return str(self.operator)

    def h(self):
        if(not(self.free)):
            return abs(self.taxi_position[0] - self.destination[0]) + abs(self.taxi_position[1] - self.destination[1])
        return abs(self.taxi_position[0] - self.passenger_position[0]) + abs(self.taxi_position[1] - self.passenger_position[1])