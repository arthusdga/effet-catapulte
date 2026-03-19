import random
from math import sqrt
import math
import numpy as np
import matplotlib.pyplot as plt



def force(pos):
    r=sqrt(pos[0]**2+pos[1]**2)
    return(-6.67*(10**(-11))*2*(10**30) / (r**3) * pos)

def initiateplanete(theta):
    Rmars=227940000000
    Vmars=24080
    posM=np.array([Rmars*math.cos(theta),Rmars*math.sin(theta)])
    vitM=np.array([-Vmars*math.sin(theta),Vmars*math.cos(theta)])
    return(posM,vitM)

def init(theta,deltav):
    mf=750000
    mM=6.418*10**23

    posf=np.array([149597870700,0])
    vitf=np.array([0,29.78*1000+deltav])

    posM,vitM=initiateplanete(theta)


    return(mf,mM,posf,vitf,posM,vitM)




"""vitf = vitf + force(posf) * dt *0.5
vitM = vitM + force(posM) * dt *0.5

for i in range(n):

    pos = pos + vit * dt
    vit = vit + force(pos)*dt"""



def distance(sys1,sys2):
    distance=sys1-sys2
    return(np.linalg.norm(distance))


def start():

    running = True
    deltav=2952.3

    mf,mM,posf,vitf,posM,vitM=init(0,deltav)


    L=[]
    n=500
    #angle0=math.pi-2.3372
    #angle0=math.pi-2.4
    angle0=0
    theta=2*math.pi/n
    dt=5000
    T=0

    for i in range(n):

        print(i)

        running= True

        mf,mM,posf,vitf,posM,vitM=init(angle0+theta*i,deltav)

        #L.append(T)
        T=0

        #Tmax=59355072.00000001
        Tmax=44616730*5/10+5000

        vitf = vitf + force(posf) * dt *0.5
        vitM = vitM + force(posM) * dt *0.5

        while ( T<Tmax) and running:

            posf = posf + vitf * dt
            vitf = vitf + force(posf)*dt

            posM = posM + vitM * dt
            vitM = vitM + force(posM)*dt

            #print(posf,posM)
            #print(distance(posf,posM))

            if distance(posf,posM)<600000000*20:     #c'est a dire inferieur au rayon d'influence
                L.append((math.pi-(angle0+theta*i),T))
                running=False
                print('win')

                """
                print(posf)
                print(posM)
                """
                #print(distance(posf,posM))

            T+=dt
    #print(posf,posM)
    #print(distance(posf,posM))
    return(L)


L=start()
if L!=[]:
    print(L)


