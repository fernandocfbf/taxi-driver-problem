from classes.SearchAlgorithms import AEstrela
from classes.TaxiSolver import TaxiSolver

def main():
    state = TaxiSolver("")
    algorithm = AEstrela()
    result = algorithm.search(state)
    if result:
        print(result.show_path())
    else:
        print("Couldn't find a solution!")

if __name__ == '__main__':
    main()