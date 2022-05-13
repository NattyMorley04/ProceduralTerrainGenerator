from matplotlib import pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import random as r

import tilesetFunctions
import voronoiFunctions
from colorama import Fore

world_size = 64
world_complexity = 50
regions = r.randint(2*world_complexity, 4*world_complexity)
points = [[world_size, world_size], [-world_size, world_size], [world_size, -world_size], [-world_size, -world_size]]

for i in range(regions):
    points.append([r.randint(0, 128), r.randint(0, 128)])

vor = Voronoi(points, qhull_options='Qbb Qc Qx')


for y in range(0, world_size):
    for x in range(0, world_size * 2):
        tileToAdd = None
        tileToAdd = tilesetFunctions.isOcean([x, y], world_size)
        if tileToAdd == "#":
            tileToAdd = tilesetFunctions.biomeCheck([x, y], world_size, regions, points)
        print(tilesetFunctions.tileToColor(tileToAdd)+tileToAdd, end="")
    print("")
plt.show()
