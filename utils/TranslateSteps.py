from constants.TaxiSolver import GYM_TRANSLATOR

def translateSteps(steps):
    return [GYM_TRANSLATOR[step] for step in steps]
