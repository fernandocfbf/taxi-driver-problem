from classes.TaxiSolver import TaxiSolver
from classes.SearchAlgorithms import AEstrela
from constants.Problems import PROBLEM1, PROBLEM2, PROBLEM3, PROBLEM4

def test01():
    state = TaxiSolver(
        operator = PROBLEM1["operator"],
        free = PROBLEM1["free"],
        taxi_position = PROBLEM1["taxi_position"],
        city_size = PROBLEM1["city_size"],
        blocked_positions = PROBLEM1["blocked_positions"], 
        passenger_position = PROBLEM1["passenger_position"],
        destination = PROBLEM1["destination"],
    )
    algorithm = AEstrela()
    result = algorithm.search(state)
    assert result.show_path() == " ; down ; right ; up ; pickup ; down"

def test02():
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
    assert result.show_path() == " ; down ; right ; right ; right ; right ; right ; right ; right ; down ; pickup ; right ; right ; down ; down ; down ; down ; down ; down ; down"

def test03():
    state = TaxiSolver(
        operator = PROBLEM3["operator"],
        free = PROBLEM3["free"],
        taxi_position = PROBLEM3["taxi_position"],
        city_size = PROBLEM3["city_size"],
        blocked_positions = PROBLEM3["blocked_positions"], 
        passenger_position = PROBLEM3["passenger_position"],
        destination = PROBLEM3["destination"],
    )
    algorithm = AEstrela()
    result = algorithm.search(state)
    assert result.show_path() == " ; down ; right ; right ; right ; right ; right ; down ; down ; down ; pickup ; left ; left ; left ; left ; left ; up ; up ; up ; up"

def test04():
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
    assert result.show_path() == " ; down ; right ; right ; right ; right ; right ; down ; down ; down ; down ; down ; down ; down ; pickup ; left ; left ; left ; left ; left ; down"