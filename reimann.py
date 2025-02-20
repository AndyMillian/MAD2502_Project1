import numpy as np

def left_endpoint(x_vals, func):
    dx = np.diff(x_vals)
    return np.sum(func(x_vals[:-1])* dx)


def trapezoid(x_vals, func):
    dx = np.diff(x_vals)
    return np.sum((dx/2)* (func(x_vals[:-1])+func(x_vals[1:])))

#def simpson(x_vals, func):


x_vals = np.linspace(0, np.pi, 10000)
func = np.sin

print(left_endpoint(x_vals, func))
print(trapezoid(x_vals, func))
#print(simpson(x_vals, func))