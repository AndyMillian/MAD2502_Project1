import numpy as np
 
# Computes the barycentric coordinates of a point with respect to a given triangle.
# Barycentric coordinates express a point as a weighted combination of a triangle's vertices.
def get_barycentric_coordinates(triangle_coordinates, point_coordinates):
    # Construct an augmented matrix with triangle coordinates and a row of ones.
    X = np.vstack([triangle_coordinates, np.ones((1, 3))])
       # Extend the point's coordinates with an additional 1 for homogeneity.
    y = np.append(point_coordinates, 1) # Shape: (3,)
     # Solve the linear system to get barycentric coordinates.
    barycentric_coords = np.linalg.solve(X, y)
    return barycentric_coords

# Converts barycentric coordinates back to Cartesian coordinates.
# This reconstructs a point in the plane using the triangle's vertices.
def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    return np.dot(triangle_coordinates, barycentric_coordinates) # Weighted sum of vertices

# Determines if a given point is inside a triangle using its barycentric coordinates.
# A point is inside if all its barycentric coordinates are non-negative.
def is_inside_triangle(triangle_coordinates, point_coordinates):
    barycentric_coords = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
     # Check if all barycentric coordinates are >= 0 (inside or on the triangle).
    return np.all(barycentric_coords >= 0)
