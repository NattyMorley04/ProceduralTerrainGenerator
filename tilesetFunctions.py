from scipy.spatial import distance
import random as r

previous_rainfall = r.randint(-1, 1)

def isOcean(coordinates, world_size):
    if distance.euclidean(coordinates, [world_size / 2, world_size / 2]) > world_size * 15/16:
        return "O"
    else:
        return "#"


def biomeCheck(coordinates, world_size):
    global previous_rainfall
    rainfall = 0
    if r.randint(0, 100) > 75:
        rainfall = r.randint(-1, 1)
    else:
        rainfall = previous_rainfall
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
