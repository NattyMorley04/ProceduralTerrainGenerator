from scipy.spatial import distance


def findRegionID(coordinates, regions, points):
    closest_index = None
    dist = float('inf')
    for i in range(0, regions):
        if float(distance.euclidean(points[i], coordinates)) < dist:
            dist = distance.euclidean(points[i], coordinates)
            closest_index = i
    return closest_index
