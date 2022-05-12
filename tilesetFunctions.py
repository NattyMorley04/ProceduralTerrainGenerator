from scipy.spatial import distance
import random as r

previous_rainfall = 0

def isOcean(coordinates, world_size):
    if distance.euclidean(coordinates, [world_size / 2, world_size / 2]) > world_size * 15/16:
        return "O"
    else:
        return "#"


def biomeCheck(coordinates, world_size):
    global previous_rainfall
    rainfall = 0
    rainfall_list = [-1, 0, 1]
    if r.randint(0, 100) > 75:
        rainfall_list.remove(previous_rainfall)
        rainfall = r.choice(rainfall_list)
        previous_rainfall = rainfall

    polar_distance = distance.euclidean(coordinates, [world_size / 8, world_size])
    if polar_distance > distance.euclidean(coordinates, [world_size / 2, 0]):
        polar_distance = distance.euclidean(coordinates, [world_size / 2, 0])

    if polar_distance > world_size / 8:
        temperature = -1
    elif polar_distance < 7 / 8 * world_size:
        temperature = 1

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
        return '\033[47m'
    elif tile == "S":
        return '\033[33m'
    elif tile == "T":
        return '\033[36;47m'
    elif tile == "V":
        return '\033[31;43m'
    elif tile == "F":
        return '\033[39;42m'
    elif tile == "M":
        return '\033[32;40m'
    elif tile == "D":
        return '\033[33;49m'
    elif tile == "J":
        return '\033[33;42m'
    elif tile == "R":
        return '\033[34;42m'
    else:
        return ""