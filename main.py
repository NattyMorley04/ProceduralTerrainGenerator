from matplotlib import pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from perlin_noise import PerlinNoise
import random as r

import locationFunctions
import tilesetFunctions
import voronoiFunctions

seed = r.randint(1,1000000)
r.seed(seed)
world_size = 64
world_complexity = 512
regions = r.randint(2*world_complexity, 4*world_complexity)
points = [[world_size, world_size], [-world_size, world_size], [world_size, -world_size], [-world_size, -world_size]]

noise = PerlinNoise(octaves=10, seed=1)

height_map = []
noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)

for j in range(world_size * 2):
    row = []
    for i in range(world_size):
        noise_val = noise1([i/world_size * 2, j/world_size])
        noise_val += 0.5 * noise2([i/world_size * 2, j/world_size])
        noise_val += 0.25 * noise3([i/world_size * 2, j/world_size])
        noise_val += 0.125 * noise4([i/world_size * 2, j/world_size])

        row.append(noise_val)
    height_map.append(row)
for i in range(regions):
    points.append([r.randint(0, 128), r.randint(0, 128)])

vor = Voronoi(points, qhull_options='Qbb Qc Qx')

current_map = []

for y in range(0, world_size):
    current_x = []
    for x in range(0, world_size * 2):
        tileToAdd = None
        tileToAdd = tilesetFunctions.heightCheck([x, y], height_map)
        if tileToAdd == "#":
            tileToAdd = tilesetFunctions.biomeCheck([x, y], world_size, points)
        if (x == 0) and (y == 0):
            tileToAdd = "X"
        current_x.append(tileToAdd)
    current_map.append(current_x)

print("Planet Name: "+locationFunctions.planetNameGenerator(seed))

for item_row in current_map:
    for item_x in item_row:
        print(tilesetFunctions.tileToColor(item_x)+item_x, end="")
    print("")
