from scipy.spatial import distance


def findRegionID(coordinates, points, precision=32 ):
    closest_index = 0
    dist = float('inf')
    while dist > precision:
        closest_index += 1
        try:
            if round(float(distance.euclidean(points[closest_index], coordinates))) < dist:
                dist = round(distance.euclidean(points[closest_index], coordinates))

        except:
            pass

    return closest_index
