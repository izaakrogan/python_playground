# derivative of Lagrangian

def dpi(x,xs):
    res = 0
    for i in xs:
        res += 1/(x-i)
    return res

def pi(x,xs,i):
    xi = xs[i]
    xs.remove(xi)
    res = 1
    for j in xs:
        res *= (x-j)/(xi-j)
    return res*dpi(x,xs)

def derLag(x,xs,ys):
    res = 0
    for i in range(len(ys)):
        res += ys[i]*pi(x,xs[:],i)
    return res

xs = [1.0,1.1,1.2,1.4,1.5]
ys = [sin(x) for x in xs]

c = derLag(1.3, xs, ys)

print(c,cos(1.3),c-cos(1.3))

print(len(ns),len(y))

res1 = list(secant(f,mpf(5),mpf(3)))

n = 0
y = []
ns = []
for x in res1:
    n += 1
    ns.append(n)
    y.append((abs(log(x-res1[-1]))/log(10))/(0.5*(1+sqrt(5)))**n)
