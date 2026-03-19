from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

m=1

dt=7.37*10**(-6)
n=int(1.e6)


pos=np.array([1,0])
vit=np.array([0,1])




Em=[]


def force(pos):
    r=sqrt(pos[0]**2+pos[1]**2)
    return(-1 / (r**3) * pos)

def em(pos,vit):
    ec=0.5 * (vit[0]**2+vit[1]**2)
    ep= - 1 / (sqrt(pos[0]**2+pos[1]**2))
    return(ep+ec)


vit = vit + force(pos) * dt *0.5

for i in range(n):

    pos = pos + vit * dt

    #Em.append(em(pos,vit))
    Em.append(em(pos,vit + (dt/2) * force(pos)))

    vit = vit + force(pos)*dt



##

Em=np.array(Em)
t=np.array([dt*i for i in range(len(Em))])

Emtheo=np.array([-0.5 for i in range(len(Em))])

plt.plot(Em, label='incertitude',   linewidth=0.5)
plt.plot(Emtheo,  label='valeur theorique')
plt.grid()

plt.legend()
plt.show()

