from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

m=1

dt=1.e-3
n=int(1.e5)


pose=np.array([1,0])
vite=np.array([0,1])


posl=np.array([1,0])
vitl=np.array([0,1])


eme=[]
eml=[]


def force(pos):
    r=sqrt(pos[0]**2+pos[1]**2)
    return(-1 / (r**3) * pos)

def em(pos,vit):
    ec=0.5 * (vit[0]**2+vit[1]**2)
    ep= - 1 / (sqrt(pos[0]**2+pos[1]**2))
    return(ep+ec)


vitl = vitl + force(posl) * dt *0.5

for i in range(n):

    pose = pose + vite * vite * dt
    posl = posl + vitl * vitl * dt

    eme.append(em(pose,vite))
    eml.append(em(posl,vitl + (dt/2) * force(posl)))

    vite = vite + force(pose)*dt
    vitl = vitl + force(posl)*dt








eme=np.array(eme)
eml=np.array(eml)
t=np.array([dt*i for i in range(len(eme))])


plt.plot(eme, label='euler')
plt.plot(eml,   label='leapfrog')
plt.legend()
plt.show()

##
plt.plot(eml-eme, label='difference')
plt.show()