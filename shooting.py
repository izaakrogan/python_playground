# Shooting ########

def f(x,yvec):
    return -yvec[0]

def G(u):
    a=array([0,u])
    ys = rungKutta4(a,0,30,40)
    return ys[-1][0]-1

def secant(f,x1,x2):
    a = [x1,x2]
    for i in range(3):
        a.append((a[-1]*f(a[-2])-a[-2]*f(a[-1]))/(f(a[-2])-f(a[-1])))
    return a

u0 = secant(G,0,1)[-1]

start = 0
finish = 30
itterations = 40
step = (start+finish)/itterations
xs = arange(start,finish+step/2,step)
ys = rungKutta4(array([0,u0]),start,finish,itterations)
plot(xs,ys)
