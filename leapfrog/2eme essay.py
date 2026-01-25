from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

m=1

dt=10**(-3)

pos=[1,0]
vit=[0,1]
acc=[-1,0]

em=[]

def pfd():
    r=sqrt(pos[0]**2+pos[1]**2)
    acc[0]-= 1 * pos[0] / (r**3)
    acc[1]-= 1 * pos[1] / (r**3)

def vitesse(dt):
    vit[0]+= acc[0]*dt
    vit[1]+= acc[1]*dt

def position(dt):
    pos[0]+= vit[0]*dt
    pos[1]+= vit[1]*dt

pfd()
vitesse(dt/2)
r=1
for i in range(1000):
    position(dt)
    r=sqrt(pos[0]**2+pos[1]**2)
    ep=-1 / r
    pfd()
    vitesse(dt/2)
    v2=vit[0]**2+vit[1]**2
    ec=1/2 * m * v2
    vitesse(dt/2)

    em.append(ep+ec)




t=[dt*i for i in range(len(em))]

t=np.array(t)
em=np.array(em)

plt.plot(em)
plt.show()

##

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

m=1

dt=10**(-3)

pos=[1,0]
vit=[0,1]
acc=[-1,0]

em0=[]

def pfd():
    r=sqrt(pos[0]**2+pos[1]**2)
    acc[0]-= 1 * pos[0] / (r**3)
    acc[1]-= 1 * pos[1] / (r**3)

def vitesse(dt):
    vit[0]+= acc[0]*dt
    vit[1]+= acc[1]*dt

def position(dt):
    pos[0]+= vit[0]*dt
    pos[1]+= vit[1]*dt


for i in range(1000):
    position(dt)
    r=sqrt(pos[0]**2+pos[1]**2)
    ep=-1 / r
    pfd()
    vitesse(dt)
    v2=vit[0]**2+vit[1]**2
    ec=1/2 * m * v2


    em0.append(ep+ec)




t=[dt*i for i in range(len(em0))]

t=np.array(t)
em0=np.array(em0)

#plt.plot(em0-em,  label='euler')
plt.plot(em0,   label='euler')
plt.legend()
plt.show()

##

plt.plot(t,em0, label='euler')
plt.plot(t,em,   label='leapfrog')
plt.legend()
plt.show()

##
plt.plot(em0-em, label='difference')
plt.show()