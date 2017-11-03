# lagragian
def pi(x,i,xs):
    xi = xs[i]
    xs.remove(xi)
    res = 1;
    for xj in xs:
        res *= (x-xj)/(xi-xj)
    return res

def lagrange(x,xs,ys):
    res = 0
    for i in range(len(ys)):
        res += ys[i]*pi(x,i,xs[:])
    return res

xs=[1,2,3,4,5,6];
ys=[0.,0.841471,0.909297,0.14112,-0.756802,-0.958924];
print(lagrange(1.5,xs,ys))
