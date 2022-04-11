from classes.SearchAlgorithms import AEstrela, BuscaGananciosa
from classes.TaxiSolver import TaxiSolver

from constants.TaxiSolver import PROBLEM1, PROBLEM2, PROBLEM3, PROBLEM4

def main():
    state = TaxiSolver(
        operator = PROBLEM4["operator"],
        free = PROBLEM4["free"],
        taxi_position = PROBLEM4["taxi_position"],
        city_size = PROBLEM4["city_size"],
        blocked_positions = PROBLEM4["blocked_positions"], 
        passenger_position = PROBLEM4["passenger_position"],
        destination = PROBLEM4["destination"],
    )
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result:
        print(result.show_path())
    else:
        print("Couldn't find a solution!")

if __name__ == '__main__':
    main()