# trapezoidal
def trapezoidal(f,a,b,n):
    fs = list(map(lambda x: f(x), np.linspace(a,b,n+1)));
    return ( sum(fs)-(fs[0]+fs[-1])*0.5)*(b-a)/n

# simpson
def simpson(f,a,b,n):
    r = np.linspace(a,b,n+1)
    total = 0
    for i in range(len(r)-1):
        total += (((b-a)/n)/6)*(f(r[i])+4*f((r[i]+r[i+1])/2)+f(r[i+1]))
    return total

def f(x):
    return 2/(x**2+1)

print(trapezoidal(f,-1.0,1.0,10.0))
print(simpson(f,-1.0,1.0,10.0))

p = 4 # run through powers and check numbers are the same
for i in range(1,20): # checking it experimentally
    print((simpson(np.cos,0.0,1.0,i)-np.sin(1.0))*(i**p))
