
# Gaussian Integration
import math
from scipy import integrate

a,b = -1,+1
def w(x):
    return math.exp(-x**2)

def h(k):
    return integrate.quad(lambda x: w(x)*x**k,a,b)[0]

def nodesAndWeights(n):
    B = np.array([[None]*(n+1)]*(n+1))
    b = np.array([None]*(n+1))
    for k in range(n+1):
        b[k] = -h(n+1+k)
        for i in range(n+1):
            B[k,i] = h(k+i)
    cs = np.linalg.solve(B,b)
    cs = np.append(cs,[1])
    xs = np.roots(cs[::-1]).real
    xs.sort()
    A = np.array([None]*(n+1))
    for k in range(n+1):
        b[k] = h(k)
        for i in range(n+1):
            B[k,i] = xs[i]**k
    As = np.linalg.solve(B,b)
    return xs, As

def gauss(f,A,x):
    return sum(A*np.array(list(map(f,x))))

xs,As = nodesAndWeights(6)
gauss(lambda x: math.exp(-x),As,xs)
