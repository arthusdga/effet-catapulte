#pb a deux corps dt?->1%
import numpy as np
import time
import matplotlib.pyplot as plt
from math import sqrt
import math

origine=[650,400]
echelle=300
dt=0.00001
t0=0
GMm=1

A=[1,[1,0],[0,1],[0,0]]
O=[0,[0,0],[0,0],[0,0]]



def forceG(A,B):
    r=0
    for i in range(2):
        r+=(A[1][i]-B[1][i])**2
    r=sqrt(r)
    ur=[]
    for i in range(2):
        ur.append((B[1][i]-A[1][i])/r)
    F=[]
    for i in range(2):
        F.append((GMm/r**2)*ur[i])
    return F

def pfd(systeme,listeF):
    sommeF=[0,0]
    for i in range(len(listeF)):
        for j in range(2):
            sommeF[j]=sommeF[j]+listeF[i][j]
    for i in range(2):
        systeme[3][i]=sommeF[i]/systeme[0]

#ordre 1 (euler)

def vitesse(systeme,dt):
    for i in range(2):
        systeme[2][i]+=systeme[3][i]*dt

def position(systeme,dt):
    for i in range(2):
        systeme[1][i]+=systeme[2][i]*dt

def traj(systeme,t):
    pfd(systeme,force(M))
    vitesse(systeme,t)
    position(systeme,t)



#energie

def ec(systeme):
    v2=systeme[2][0]**2+systeme[2][1]**2
    m=systeme[0]
    return(1/2*m*v2)

def epp(A,B):
    m=A[0]
    r=0
    for i in range(2):
        r+=(A[1][i]-B[1][i])**2
    r=sqrt(r)
    for i in range(2):
        epp=-GMm/r
    return epp

def em(A,B):
    return(ec(A)+epp(A,B))


x = []
y = []

plt.ion()

figure, ax = plt.subplots(figsize=(8, 6))
plt.axis([-1, 10**3,-0.5-10**(-5),-0.5+10**(-5)])
plt.grid(True)

(line1,) = ax.plot(x, y)

plt.title("Dynamic Plot Em(x) ordre1", fontsize=25)

plt.xlabel("t/dt (dt="+str(dt)+")", fontsize=18)
plt.ylabel("Em (graduation a 10**-5)", fontsize=18)

print('pour zoomer:clique droit+bouger la souris')

for p in range(10**10):
    x = x+[p]
    y = y+[em(A,O)]

    pfd(A,[forceG(A,O)])
    vitesse(A,dt)
    position(A,dt)

    line1.set_xdata(x)
    line1.set_ydata(y)

    figure.canvas.draw()

    figure.canvas.flush_events()
    #time.sleep(0.001)

plt.pause(1800)
plt.close()

