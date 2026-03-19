#terrain de jeu

import pygame
import random
from math import sqrt
import math
import numpy as np

from pygame.locals import *
import matplotlib.pyplot as plt

#forcee


def nforces(M):
    n=len(M)
    F=[[]for i in range(n)]
    for i in range(n):
        F[i].append(forceG(O,M[i]))
        for j in range(i+1,n):
            f=forceG(M[j],M[i])
            F[i].append(f)
            F[j].append([-f[0],-f[1]])
    return(F)

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





def initiateplanete(theta):
    global O
    O=[2*10**30,[0,0],[0,0],[0,0]]
    Rmars=227940000000
    Vmars=24080
    M=[

    [5.972*10**24,[149597870700,0],[0,29.78*1000],[0,0]],  #terre
    [6.418*10**23,[Rmars*math.cos(theta),Rmars*math.sin(theta)],[-Vmars*math.sin(theta),Vmars*math.cos(theta)],[0,0]]  #mars

    ]
    return(O,M)


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

def distance(sys1,sys2):
    return(sqrt((sys1[1][0]-sys2[1][0])**2+(sys1[1][1]-sys2[1][1])**2))

#on va lui donner du carburant. il faut set une quantite de carburant maximale et le poids a vide, modifier sa masse en fonction de la pousse

#objectif 1: ellipse de Hohmann pour aller sur mars

#objectif 2: quitter le plus vite possible en dehors du systeme solaire, regarder les accelerations subies (4-6g max)

# rajouter une variable qui calcule le temps de trajet



# controle

def start():
    global origine
    global couleur,fusee,tpousse,fpoussee
    global g,t,t0

    initiaterepere()
    O,M=initiateplanete(0)
    initiatefusee()

    running = True
    play=True
    poussee=False
    deltav=2952.3

    pause=1800

    C=[]
    L=[]
    n=1000
    angle0=math.pi-2.3372
    theta=0.01/n
    for i in range(n):
        running= True
        initiateplanete(angle0+theta*i)
        initiatefusee()
        T=0
        npoussee(deltav)
        vitesse=deltav-1
        while ( T<80000) and running:
        #pfd
            #traj(M[0],t)
            traj(M[1],t)
            traj(fusee,t)


            vitesse=sqrt(fusee[2][0]**2+fusee[2][1]**2)

            if distance(fusee,M[1])<600000000:     #c'est a dire inferieur au rayon d'influence
                L.append((math.pi-(angle0+theta*i),T))
                running=False
            T+=t     #/31536000
        #print(i)
    return(L)


L=start()
if L!=[]:
    print(L)


