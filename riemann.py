import numpy as np

def left_endpoint(x_vals, func):
    dx = np.diff(x_vals)
    return np.sum(func(x_vals[:-1])* dx)

def trapezoid(x_vals, func):
    dx = np.diff(x_vals)
    return np.sum((dx/2)* (func(x_vals[:-1])+func(x_vals[1:])))

def simpson(x_vals, func):
    dx = np.diff(x_vals)[0]
    return (dx/3) * (func(x_vals)[0]+4 * np.sum(func(x_vals)[1:-1:2])+2 * np.sum(func(x_vals)[2:-2:2])+func(x_vals)[-1])