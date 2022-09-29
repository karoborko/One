import random as rd
import numpy as np


def polarcoordinates(k):
    """the function generates random polar coordinates of k points lying in a unit circle"""
    assert k > 0, "function cannot create less than 1 point"
    polar_points = []  # creating empty list for k points
    for i in range(k):  # genereting k points
        point = []  # creating empty list for point coordinates
        r = rd.uniform(0.0, 1.0)
        point.append(r)
        theta = rd.uniform(0.0, 2.0 * np.pi)
        point.append(theta)
        assert point != [], "point cannot have no coordinates"
        polar_points.append(point)  # adding point to point list
    assert polar_points != [], "after executing the function, the list must contain at least 1 point"
    return polar_points


def from_polar_to_cartesian(polar_points):
    """the function converts the polar coordinates of a point into Cartesian coordinates"""
    assert polar_points != [], "the entered list of points cannot be empty"
    cartesian_points = []  # creating empty list for converted k points
    for i in range(len(polar_points)):
        point = []
        x = polar_points[i][0] * np.cos(polar_points[i][1])  # np.cos to funkcja cosinus

        assert x <= 1.0, "x coordinate cannot be larger than 1"
        assert x >= -1.0, "x coordinate cannot be lesser than -1"
        point.append(x)
        y = polar_points[i][0] * np.sin(polar_points[i][1])
        assert y <= 1.0, "y coordinate cannot be larger than 1"
        assert y >= -1.0, "y coordinate cannot be lesser than -1"
        point.append(y)
        assert point != [], "point cannot have no coordinates"
        cartesian_points.append(point)
    assert cartesian_points != [], "after executing the function, the list must contain at least 1 point"
    return cartesian_points


if __name__ == '__main__':
    print("Function tests: ")
    test_polar_points = polarcoordinates(10)
    for i in range(10):
        assert test_polar_points[i][0] >= 0.0 and test_polar_points[i][0] <= 1.0, "Error! Function draws wrong radius"
        assert test_polar_points[i][1] >= 0.0 and test_polar_points[i][
            1] <= 2.0 * np.pi, "Error! Function draws wrong theta angle"
    test_cartesian_points = from_polar_to_cartesian(test_polar_points)
    for i in range(10):
        assert test_cartesian_points[i][0] ** 2 + test_cartesian_points[i][
            1] ** 2 <= 1, "Error! The transforms of points is incorrect"
        # the distance of the transformed points cannot be greater than 1 (because they are always in a single circle)