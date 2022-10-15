# brute force approach to find the 2D maxima and minima set of points in given points

def maxima(points):
    maxima_set = []
    for point in points:
        maxima = True
        for other in points:
            if point != other and point[0] <= other[0] and point[1] <= other[1]:
                maxima = False
                break
        if (maxima == True):
            maxima_set.append(point)
    print(maxima_set)


def minima(points):
    maxima_set = []
    for point in points:
        maxima = True
        for other in points:
            if point != other and point[0] >= other[0] and point[1] >= other[1]:
                maxima = False
                break
        if (maxima == True):
            maxima_set.append(point)
    print(maxima_set)


if __name__ == '__main__':
    points = [(2, 1), (4, 1), (6, 1), (2, 2), (3, 2),
              (2, 3), (1, 4), (5, 4), (3, 5), (2, 7)]
    maxima(points)
    minima(points)
