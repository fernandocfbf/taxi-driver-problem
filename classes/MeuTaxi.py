import numpy as np

from constants.TaxiSolver import TARGET_POINTS

from classes.TaxiSolver import TaxiSolver
from utils.AdjusteRightLeft import adjustRightLeft
from utils.TranslateColumns import translateColumns
from utils.GetTargetPoints import getTargetPoints
from utils.TranslateSteps import translateSteps

from classes.SearchAlgorithms import AEstrela



class MeuTaxi():
    def __init__(self, map, positions):
        positions_to_list = list(positions)
        city = np.zeros((map.shape[0], map.shape[1])).astype(str)
        target_points_position = getTargetPoints(map, city, TARGET_POINTS)
        init = [positions_to_list[0] + 1, translateColumns(positions_to_list[1])]
        self.state = TaxiSolver("",
            True,
            init,
            5,
            map,
            target_points_position[positions_to_list[2]],
            target_points_position[positions_to_list[3]]
            )
        algorithm = AEstrela()
        self.result = algorithm.search(self.state)

    def path(self):
        if self.result != None:
            print(self.result.show_path())
            steps = (self.result.show_path()+";dropoff").replace(" ","").replace(";"," ").split() 
            adjust_steps = adjustRightLeft(steps)
            solution = translateSteps(adjust_steps)
            return solution
        else:
            return 'Nao achou solucao'