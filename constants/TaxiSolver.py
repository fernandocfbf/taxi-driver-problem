POSSIBILITIES = {
    "down": [0,  1],
    "up": [0, -1],
    "left":  [-1, 0],
    "right":  [1,  0],
}

PROBLEM1 = {
    "operator": " ",
    "free": True,
    "taxi_position": [0, 0],
    "city_size": 2,
    "blocked_positions": [], 
    "passenger_position": [0, 1],
    "destination": [1, 1]
}

PROBLEM2 = {
    "operator": " ",
    "free": True,
    "taxi_position": [0, 0],
    "city_size": 10,
    "blocked_positions": [[0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4]], 
    "passenger_position": [2, 7],
    "destination": [9, 9]
}