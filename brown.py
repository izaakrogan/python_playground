############ brownian

import numpy as np

def brown(T,s):
    zs = np.arange(0,T,0.001)
    xs=np.zeros(zs.size)
    xs[0]=0
    sq = np.sqrt(0.001)
    for i in np.arange(1,zs.size):
        xs[i] = xs[i-1] + s*np.random.normal(0,sq)
    return zs, xs

import matplotlib.pyplot as plt
zs, xs = brown(1,1)
# plt.plot(zs, xs)
# plt.show()

ys = np.zeros(100)
T=1

for i in range (100):
    zs, xs = brown(T,1)
    ys[i]=xs[-1]
    # plt.plot(zs, xs,"b")
    # plt.show()

from scipy.stats.kde import gaussian_kde
kde = gaussian_kde(ys)
xs = np.arange(-5,5,0.1)
plt.plot(xs,kde(xs))
plt.plot(xs,np.exp(-xs*xs/2/T)/np.sqrt(2*np.pi*T))
plt.show()
