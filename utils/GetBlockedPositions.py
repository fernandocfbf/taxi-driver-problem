import numpy as np
from constants.TaxiSolver import BLOCKED_SYMBOLS

from utils.GetTargetPoints import getTargetPoints

def getBlockedPositions(map):
    if type(map) != list:
        city = np.zeros((map.shape[0], map.shape[1])).astype(str)
        target_points_position = getTargetPoints(map, city, BLOCKED_SYMBOLS)
        return target_points_position
    return map