# polynomial fit
def findfit(m,xs,ys):
    A = np.zeros((m+1,m+1))
    b = np.zeros(m+1)
    for k in range(m+1):
        b[k] = sum(ys*xs**k)
        for j in range(m+1):
            A[k,j] = sum(xs**(k+j))
    sol = np.linalg.solve(A,b)
    def fit(x):
        a = 0
        for i in range(m+1):
            a += sol[i]*x**i
        return a
    return fit

import numpy as np

xs = np.array ([1 ,2 ,3 ,4 ,5 ,6])
ys = np.array ([-5.21659,2.53152,2.05687,14.1135,20.9673,33.5652])

ft = findfit(2,xs,ys)

# fit with basis

# first define a list of functions
basis = [lambda x: cos(2*pi*0*x),
        lambda x: sin(2*pi*1*x),
        lambda x: cos(2*pi*1*x),
        lambda x: sin(2*pi*2*x),
        lambda x: cos(2*pi*2*x)]

# each element of this list is a function
basis[3](1/10)

# then modify a bit the code from lectures
def findfitWithBasis(m,xs,ys):
    A = zeros([m+1,m+1])
    b = zeros(m+1)
    for k in range(m+1):
        b[k] = sum(ys*basis[k](xs)) # change here
        for j in range(m+1):
            A[k,j] = sum(basis[k](xs)*basis[j](xs)) # and here
    a = linalg.solve(A,b)
    def fit(x):
        res = 0
        for i in range(m+1):
            res = res + a[i]*basis[i](x)
        return res
    return fit

datax = arange(1,13)/12
datay = array([9.2,8.7,8.2,9.6,11.4,13.6,15.4,16.9,17.3,16.3,14.7,12])
ft=findfitWithBasis(3,datax,datay)

xs = linspace(0,1)
ys = list(map(ft,xs))
plot(xs,ys,'b')
plot(datax,datay,'or')

# finding the maximum approximatelly from the picture
[ft(0.72),ft(0.74),ft(0.73)]

(0.74*12-8)*30
# which is ~26 august
