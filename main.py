from classes.SearchAlgorithms import AEstrela, BuscaGananciosa
from classes.TaxiSolver import TaxiSolver

from constants.TaxiSolver import PROBLEM1, PROBLEM2

def main():
    state = TaxiSolver(
        operator = PROBLEM2["operator"],
        free = PROBLEM2["free"],
        taxi_position = PROBLEM2["taxi_position"],
        city_size = PROBLEM2["city_size"],
        blocked_positions = PROBLEM2["blocked_positions"], 
        passenger_position = PROBLEM2["passenger_position"],
        destination = PROBLEM2["destination"],
    )
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result:
        print(result.show_path())
    else:
        print("Couldn't find a solution!")

if __name__ == '__main__':
    main()