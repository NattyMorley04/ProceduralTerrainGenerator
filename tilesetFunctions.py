from scipy.spatial import distance
import random as r

import voronoiFunctions

previous_rainfall = 0

def isOcean(coordinates, world_size):
    if distance.euclidean(coordinates, [world_size/2, world_size]) > world_size * 2:
        return "O"
    else:
        return "#"


def biomeCheck(coordinates, world_size, regions, points):
    global previous_rainfall
    region_id = voronoiFunctions.findRegionID(coordinates, points) 

    if region_id % 3 == 0:
        rainfall = 0
    elif region_id % 3 == 1:
        rainfall = -1
    elif region_id % 3 == 2:
        rainfall = 1
    if (coordinates[1] > world_size * 15/16) or (coordinates[1] < world_size * 1/16):
        temperature = -3
    elif world_size * 3/8 < coordinates[1] < world_size * 5/8:
        temperature = 1
    elif (coordinates[1] > world_size * 7/8) or (coordinates[1] < world_size * 1/8):
        temperature = -1
    else:
        temperature = 0
        rainfall = 0

    if region_id % 2 == 0 and temperature != -3:
        if r.randint(0, 100) < 95:
            return "O"

    if r.randint(0,100) > 95:
        return "O"

    if temperature == -1:
        if rainfall == -1:
            return "T"
        elif rainfall == 0:
            return "I"
        elif rainfall == 1:
            return "S"
        elif temperature == -3:
            return "A"
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
    elif temperature == -3:
        return "A"
    else:
        return "#"

def tileToColor(tile):
    if tile == "X":
        return '\033[35m'
    elif tile == "A":
        return '\033[39;49m'
    elif tile == "S":
        return '\033[39;49m'
    elif tile == "I":
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