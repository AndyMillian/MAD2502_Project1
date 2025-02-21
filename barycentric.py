import numpy as np

def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    X = np.vstack([triangle_coordinates, np.ones((1, 3))])
    y = np.append(point_coordinates, 1)
    barycentric_coords = np.linalg.solve(X, y)
    return barycentric_coords

def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    return np.dot(triangle_coordinates, barycentric_coordinates)

def is_inside_triangle(triangle_coordinates, point_coordinates):
    barycentric_coords = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    return np.all(barycentric_coords >= 0)
