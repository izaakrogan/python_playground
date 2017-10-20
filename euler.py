# Euler ################

def f(x,ys):
    return -ys[0]

def foo(x,ys):
    n = ys.size
    res = zeros(n)
    for i in range(n-1):
        res[i] = ys[i+1]
    res[n-1] = f(x,ys)
    return res

def Eulr(initial,a,b,itt):
    h = (b-a)/itt
    n = initial.size
    ys = zeros((itt+1,initial.size))
    ys[0] = initial
    for i in range(itt):
        ys[i+1] = ys[i] + h*foo(a+i*h,ys[i])
    return ys

def rungKutta(initial,a,b,itt):
    h = (b-a)/itt
    ys = zeros((itt+1,initial.size))
    ys[0] = initial
    for i in range(itt):
        ys[i+1]=ys[i]+h/2*(foo(a+i*h,ys[i])+foo(a+i*h+h,ys[i]+h*foo(a+i*h,ys[i])))
    return ys

def rungKutta4(initial,a,b,itt):
    h = (b-a)/itt
    n = initial.size
    ys = zeros((itt+1,initial.size))
    ys[0] = initial
    for i in range(itt):
        o = a+i*h
        n1 = h*foo(o,ys[i])
        n2 = h*foo(o+h/2,ys[i]+n1/2)
        n3 = h*foo(o+h/2,ys[i]+n2/2)
        n4 = h*foo(o+h,ys[i]+n3)
        ys[i+1] = ys[i]+(n1+2*n2+2*n3+n4)*1/6
    return ys

start = 0
finish = 30
itterations = 40
step = (start+finish)/itterations
xs = arange(start,finish+step/2,step)
ys = rungKutta4(array([0,1]),start,finish,itterations)
plot(xs,ys)
plot(xs,[sin(x) for x in xs])
