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
    elif tile == "T":
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
    elif tile == "─":
        return '\033[34;49m'
    elif tile == "│":
        return '\033[34;49m'
    elif tile == "┼":
        return '\033[34;49m'
    else:
        return ""

def addRivers(coordinates, world_length):
    map_with_rivers = coordinates
    for row in range(0, len(coordinates)-1):
        counter = 0
        for item_x in coordinates[row]:
            if item_x != "O":
                if r.randint(0, 100) == 1:
                    if r.randint(0, 1) == 1:
                        map_with_rivers[row][counter] = "─"
                    else:
                        map_with_rivers[row][counter] = "│"
                elif counter != 0 and (counter != world_length - 1):
                    if ((coordinates[row][counter - 1] == "─") or (coordinates[row][counter - 1] == "│") \
                            or (coordinates[row - 1] == "┼")) and (r.randint(0, 1) == 0):
                        map_with_rivers[row][counter] = "─"
                if row != 0:
                    if ((coordinates[row - 1][counter] == "─") or (coordinates[row - 1] == "│") \
                            or (coordinates[row - 1] == "┼")) and (r.randint(0, 1) == 0):
                        map_with_rivers[row][counter] = "│"
            counter += 1
    map_with_rivers = riverCornerCheck(map_with_rivers, world_length)
    return map_with_rivers

def riverCornerCheck(world_map, world_size):
    map_with_river_check = world_map
    for y in range(0, len(world_map) - 1):
        for x in range(0, len(world_map) - 1):
            if (map_with_river_check[x][y] == "─") or (map_with_river_check[x][y] == "│"):
                if (y != 0) and (x != 0) and (y != world_size - 1) and (x != world_size - 1):
                    if (map_with_river_check[y][x - 1] == "─") and (map_with_river_check[y - 1][x] == "│"):
                        map_with_river_check[y][x] = "┼"
                    elif (map_with_river_check[y][x + 1] == "─") and (map_with_river_check[y - 1][x] == "│"):
                        map_with_river_check[y][x] = "┼"
                    elif (map_with_river_check[y][x + 1] == "─") and (map_with_river_check[y + 1][x] == "│"):
                        map_with_river_check[y][x] = "┼"
                    elif (map_with_river_check[y][x - 1] == "─") and (map_with_river_check[y + 1][x] == "│"):
                        map_with_river_check[y][x] = "┼"
    return map_with_river_check