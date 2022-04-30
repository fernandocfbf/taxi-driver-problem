from constants.TaxiSolver import TARGET_POINTS

def getTargetPoints(map, city, list_targets):
    res = list()
    for i in range(city.shape[0]):
        for j in range(city.shape[1]):
            city[i,j] = str(map[i,j].decode('UTF-8'))
            if city[i,j] in list_targets:
                res.append([i,j])
    return res
