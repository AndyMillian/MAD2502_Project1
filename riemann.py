import numpy as np # Import NumPy for numerical computations

# Approximates the integral of a function using the Left Endpoint Rule.
# This method estimates the area under the curve by summing up rectangles 
# with heights determined by the function values at the left endpoints of subintervals.

def left_endpoint(x_vals, func):
    dx = np.diff(x_vals)# Compute the width of each subinterval
    return np.sum(func(x_vals[:-1])* dx) # Multiply function values at left endpoints by dx and sum up

# Approximates the integral using the Trapezoidal Rule.
# This method estimates the area by summing up trapezoids instead of rectangles, 
# using the average of function values at the left and right endpoints.
def trapezoid(x_vals, func):
    dx = np.diff(x_vals) # Compute the width of each subinterval
    return np.sum((dx/2)* (func(x_vals[:-1])+func(x_vals[1:])))  # Apply the trapezoidal formula


# Approximates the integral using Simpson's Rule.
# This method provides a more accurate estimate by fitting quadratic functions (parabolas) 
# through points instead of straight-line approximations.
def simpson(x_vals, func):
    dx = np.diff(x_vals)[0] 
    return (dx/3) * (func(x_vals)[0]+4 * np.sum(func(x_vals)[1:-1:2])+2 * np.sum(func(x_vals)[2:-2:2])+func(x_vals)[-1])
