import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans



def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(sy.exp(-x**2) * sy.cos(x), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[2,3,5,-2,-3,-6,0,0,0,0], [3,4,4,-3,-1,4,0,0,0,0]
    ,[5,4,10,6,-4,22,0,0,0,0],[-2,-3,6,4,0,12,-2,3,6,0]
    ,[-3,-1,-4,0,2,0,3,-1,4,0],[-6,4,22,12,0,90,-6,-4,22,0],[0,0,0,-2,3,-6,2,-3,5,5]
    ,[0,0,0,3,-1,-4,-3,4,-4,0],[0,0,0,6,4,22,5,-4,10,26]
    ,[0,0,0,0,0,0,5,0,26,53]] )
    b = np.array([3,-6,-170,0,-13,0,0,-7,170,0])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1200667
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())