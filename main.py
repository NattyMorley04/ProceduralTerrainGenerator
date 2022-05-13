from matplotlib import pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import random as r

import locationFunctions
import tilesetFunctions
import voronoiFunctions

seed = r.randint(1, 1000000)
r.seed(seed)
world_size = 64
world_complexity = 64
regions = r.randint(2*world_complexity, 4*world_complexity)
points = [[world_size, world_size], [-world_size, world_size], [world_size, -world_size], [-world_size, -world_size]]

for i in range(regions):
    points.append([r.randint(0, 128), r.randint(0, 128)])

vor = Voronoi(points, qhull_options='Qbb Qc Qx')

current_map = []

for y in range(0, world_size):
    current_x = []
    for x in range(0, world_size * 2):
        tileToAdd = None
        tileToAdd = tilesetFunctions.isOcean([x, y], world_size)
        if tileToAdd == "#":
            tileToAdd = tilesetFunctions.biomeCheck([x, y], world_size, regions, points)
        if (x == 0) and (y == 0):
            tileToAdd = "X"
        current_x.append(tileToAdd)
    current_map.append(current_x)

print("Planet Name: "+locationFunctions.planetNameGenerator(seed))

current_map = tilesetFunctions.addRivers(current_map, world_size)

def displayMap(current_map):
    for item_row in current_map:
        for item_x in item_row:
            print(tilesetFunctions.tileToColor(item_x)+item_x, end="")
        print("")

displayMap(current_map)
plt.show()
