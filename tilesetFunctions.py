from scipy.spatial import distance
import random as r

previous_rainfall = 0

def isOcean(coordinates, world_size):
    if distance.euclidean(coordinates, [world_size / 2, world_size]) > world_size * 2:
        return "O"
    else:
        return "#"


def biomeCheck(coordinates, world_size):
    global previous_rainfall
    rainfall = 0
    if r.randint(0, 100) > 75:
        rainfall = r.randint(-1,1)
        previous_rainfall = rainfall

    if world_size * 3/8 < coordinates[1] < world_size * 5/8:
        temperature = 1
    elif (coordinates[1] > world_size * 7/8) or (coordinates[1] < world_size * 1/8):
        temperature = -1
    else:
        temperature = 0

    if temperature == -1:
        if rainfall == -1:
            return "A"
        elif rainfall == 0:
            return "S"
        elif rainfall == 1:
            return "T"
        else:
            return "#"
    elif temperature == 0:
        if rainfall == -1:
            return "V"
        elif rainfall == 0:
            return "F"
        elif rainfall == 1:
            return "M"
        else:
            return "#"
    elif temperature == 1:
        if rainfall == -1:
            return "D"
        elif rainfall == 0:
            return "J"
        elif rainfall == 1:
            return "R"
        else:
            return "#"
    else:
        return "#"

def tileToColor(tile):
    if tile == "A":
        return '\033[39;49m'
    elif tile == "S":
        return '\033[39;49m'
    elif tile == "T":
        return '\033[36;49m'
    elif tile == "V":
        return '\033[31;49m'
    elif tile == "F":
        return '\033[32;49m'
    elif tile == "M":
        return '\033[32;49m'
    elif tile == "D":
        return '\033[33;49m'
    elif tile == "J":
        return '\033[32;49m'
    elif tile == "R":
        return '\033[32;49m'
    elif tile == "O":
        return '\033[34;49m'
    else:
        return ""