import matplotlib.pyplot as plt
from mpmath import *
mp.dps = 100
print(pi)

def newtonHP(f,df,x0,precision):
    n = 0;
    x = [x0];
    while (abs(f(x[n]))>10**(-precision)) and (n<100):
        n = n + 1;
        x.append(x[n-1]-f(x[n-1])/df(x[n-1]))
    return x

# root of a function by bisection
def bisection(f,a,b):
    for i in range(1000):
        c = (a+b)/2
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c

def secant(f,x1,x2):
    a = [x1,x2]
    for i in range(16):
        a.append((a[-1]*f(a[-2])-a[-2]*f(a[-1]))/( f(a[-2])-f(a[-1])))
    return a
