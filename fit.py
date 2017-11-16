# fit the data with the functions

xs = array([1,2,3,4,5])
ys = array([0,3,-2,-5,3])
fs = [sin,cos,lambda x:sin(2*x),lambda x:cos(2*x)]

A = zeros([4,4])
b = zeros(4)
for i in range(4):
    b[i] = sum(fs[i](xs)*ys)
    for j in range(4):
        A[i,j] = sum(fs[i](xs)*fs[j](xs))
a = solve(A,b)

def fit(x):
    return sum([a[i]*fs[i](x) for i in range(4)])

xdence = linspace(0.5,5.5)
plot(xdence,[fit(x) for x in xdence])
plot(xs,ys,"rx")

def rot(A):
    return transpose(A[::-1])
rot([[1,2,3],[4,5,6],[7,8,9]])

# dblquad
def f(y,x):
    return sin(2*x**2+y**2)
def lowerlimit(y):
    return 0
def upperlimit(y):
    return 1

scipy.integrate.dblquad(f,0,2,lowerlimit,upperlimit)

def f(z,y,x): # important f of y then x , not of x then y! (see conventions in the help)
    return sin(2*x**2+y**2+z**3)

def lowerlimit(y):
    return 0
def upperlimit(y):
    return 1
def lowerlimit2(z,y):
    return 2
def upperlimit2(z,y):
    return 5

scipy.integrate.tplquad(f,0,2,lowerlimit,upperlimit,lowerlimit2,upperlimit2)

N = 5
def f(t, x):
    return np.exp(-x*t) / t**N
integrate.nquad(f, [[1, np.inf],[0, np.inf]])

def f(x, y):
    return x*y
def bounds_y():
    return [0, 0.5]
def bounds_x(y):
    return [0, 1-2*y]
integrate.nquad(f, [bounds_x, bounds_y])

# Interpolate sin(x) with x=[1,1.1,1.2,1.4,1.5] by a polynomial.
# Compute the derivative of this polynomial at $x=1.3 and compare with the exact result.

xs = [1,1.1,1.2,1.4,1.5]
ys = [sin(x) for x in xs]
def dPi(i,x,xs):
    res = 0
    for j in range(len(xs)):
        if i!=j:
            res = res+1/(x-xs[j])
    return res*Pi(i,x,xs)

res = 0
x0 = 1.3
for i in range(len(xs)):
    res = res + ys[i]*dPi(i,x0,xs)
print(res,cos(x0),res-cos(x0))
