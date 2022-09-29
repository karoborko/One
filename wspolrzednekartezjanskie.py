import random as r


def cartesiancoordinates(k, l):
    """the function draws and returns the coordinates of the k Cartesian points for the l-dimension"""
    assert k > 0, "cannot create less than 1 point"
    assert l >= 2, "points are created for the space of min. 2-dimensional"
    k_points = []
    for i in range(k):
        point = []
        for j in range(l):
            x = r.uniform(-1.0, 1.0)
            point.append(x)
            assert point != [], "point cannot have no coordinates"
        k_points.append(point)
    assert k_points != [], "after executing the function, the list of points cannot be empty (at least 1 point had to be created)"
    return k_points


if __name__ == '__main__':
    print("Function tests: ")
    test_points_2D = cartesiancoordinates(10, 2)
    for i in range(10):
        assert test_points_2D[i][0] >= -1.0 and test_points_2D[i][
            0] <= 1.0, "Error! the function does not randomize the coordinates in the range -1.0 to 1.0"
        assert test_points_2D[i][1] >= -1.0 and test_points_2D[i][
            1] <= 1.0, "Error! the function does not randomize the coordinates in the range -1.0 to 1.0"
        assert test_points_2D[i][0] ** 2 + test_points_2D[i][
            1] ** 2 <= 2, "the sum of points sqrt cannot be greater than 2"
