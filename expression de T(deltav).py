#different deltav

import pygame
import random
from math import sqrt
import math
import numpy as np

from pygame.locals import *
import matplotlib.pyplot as plt

#forcee


def force(M):
    n=len(M)
    FO=[]
    for i in range(n):
        FO.append(forceG(M[i],O))
    return(FO)

def Ffusee(M):
    n=len(M)
    Ff=[forceG(O,fusee)]
    for i in range(n):
        Ff.append(forceG(M[i],fusee))
    return(FO)


# trajectoire

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
        F.append((-6.67*10**(-11)*A[0]*B[0]/r**2)*ur[i])
    return F

def pfd(systeme,listeF):
    sommeF=[0,0]
    for i in range(len(listeF)):
        for j in range(2):
            sommeF[j]+=listeF[i][j]
    for i in range(2):
        systeme[3][i]=sommeF[i]/systeme[0]

def vitesse(systeme,dt=100000):
    for i in range(2):
        systeme[2][i]+=systeme[3][i]*dt

def position(systeme,dt=100000):
    for i in range(2):
        systeme[1][i]+=systeme[2][i]*dt

def traj(systeme,t):
    pfd(systeme,[forceG(O,systeme)])
    vitesse(systeme,t)
    position(systeme,t)

def trajM(planetes,t):
    n=len(planetes)
    F=nforces(planetes)
    for i in range(n):
        pfd(planetes[i],F[i])
        vitesse(planetes[i],t)
        position(planetes[i],t)


#initialisation

#fonction de recuperation des differentes positions, vitesses, et acceleration des planetes,(et masses) sur internet

origine=[]
g=0
t=0
t0=0
T=0

O=[2*10**30,[0,0],[0,0],[0,0]]




def initiaterepere():
    global origine,g,t,t0,T
    origine=[650,400]
    g=5*10**(-10)
    t=50
    t0=0           #sert pour stopper le temps
    T=0


#fusee

#on prends l'exemple de le fusee ariane : poids fusee=270 000kg
#                                         carburant=480 000kg

fusee=[]
tpoussee=0
fpoussee=0

def initiatefusee():
    global fusee,tpousse,fpoussee
    fusee=[750000,[149597870700,0],[0,29.78*1000],[0,0]]
    tpoussee=0
    fpoussee=0

def npoussee(deltav):
    global fusee,t              #norme de la pousse uniquement
    r=0
    for i in range(2):
        r+=(O[1][i]-fusee[1][i])**2
    r=sqrt(r)
    uo=[]
    for i in range(2):
        uo.append((O[1][i]-fusee[1][i])/r)
    uo[0],uo[1]=uo[1],-uo[0]
    for i in range(2):
        fusee[2][i]+=deltav*uo[i]


#on va lui donner du carburant. il faut set une quantite de carburant maximale et le poids a vide, modifier sa masse en fonction de la pousse

#objectif 1: ellipse de Hohmann pour aller sur mars

#objectif 2: quitter le plus vite possible en dehors du systeme solaire, regarder les accelerations subies (4-6g max)

# rajouter une variable qui calcule le temps de trajet



# controle

def start(n):
    global origine,O
    global couleur,fusee,tpousse,fpoussee
    global g,t,t0

    initiaterepere()
    initiatefusee()

    running = True
    play=True
    poussee=False
    deltavmin=2952.3
    deltavmax=12369.14052
    deltavmax+=80000

    deltav=deltavmin
    vn=(deltavmax-deltavmin)/n

    v=[]
    vtot=[]
    Ttot=[]


    for i in range(n):


        initiatefusee()
        r=sqrt(fusee[1][0]**2+fusee[1][1]**2)
        T=0

        deltav+=vn
        npoussee(deltav)

        while r<227940000000:

        #pfd

            traj(fusee,t)


            r=sqrt((fusee[1][0]**2+fusee[1][1]**2))
            x=fusee[1][0]
            y=fusee[1][1]
            vx=fusee[2][0]
            vy=fusee[2][1]
            theta=math.atan(y/x)
            gamma=math.pi+math.atan(vy/vx)
            vB=sqrt(vx**2+vy**2-2*vx*vy*math.cos(theta-gamma))
            deltavB=sqrt(vB**2+21536**2)
            T+=t

        v.append(deltav)
        vtot.append(deltav+deltavB)
        Ttot.append(T)

    return(v,vtot,Ttot)

v,vtot,T=start(1000)

## afficher les resultats

Δm=[]
for k in v:
    Δm.append(750000*(math.exp(k/29.78/1000)-1))

Δmtot=[]
for k in vtot:
    Δmtot.append(750000*(math.exp(k/29.78/1000)-1))

plt.plot(v, Δm, label="Δm(Δv)", color="green", linestyle="-")
plt.plot(vtot, Δmtot, label="Δm(Δv)", color="green", linestyle="-")

plt.plot(  vtot, T,label="T(Δvtot)", color="blue", linestyle="-")
plt.plot( v, T, label="T(Δv)", color="red", linestyle="-")
plt.title("evolution du temps de transfert en fonction du deltav total")
plt.xlabel("Axe Δv")
plt.ylabel("Axe T")
#plt.xscale('log')
plt.legend()
plt.grid(True)
plt.show()


