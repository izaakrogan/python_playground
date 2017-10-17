# monte-carlo

n=0
N=10000

for i in range(N):
    x = random.uniform(−1,1)
    y = random.uniform(−1,1)
    if (x**2+ y**2<1):
        n = n+1

p1 = n/N
S1 = p1*2*2
error=2*2*sqrt(p1*(1−p1))/(sqrt(N))

N=1000
n=0
for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    z = random.uniform(-1,1)
    w = random.uniform(-1,1)
    if (x**2+y**2+z**2+w**2<1):
        n = n + 1
S1=2**4*n/N
S2=2**4-S1
(S1,pi**2/2,"error~",sqrt(S1*S2/N),"error in fact=",abs(pi**2/2-S1))
