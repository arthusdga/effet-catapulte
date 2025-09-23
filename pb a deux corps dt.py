#pb a deux corps dt?->1%
import pygame
from math import sqrt
import math
from pygame.locals import *
import numpy as np

origine=[650,400]
echelle=300
dt=0.1
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

#ordre 1

def vitesse(systeme,dt=100000):
    for i in range(2):
        systeme[2][i]+=systeme[3][i]*dt

def position(systeme,dt=100000):
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

EppA=[epp(A,O)]
EcA=[ec(A)]
xt=[0]
i=0

"""pygame.init()
font = pygame.font.Font(None, 74)  # Police par défaut, taille 74
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Terrain de jeu/fleche/o/p/m/a/z/r")
clock = pygame.time.Clock()"""
"""print('dt est '+str(dt))
print("quelles duree de l'experience voulez vous")"""
temps=100000
T=temps
while T>=0:
    """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            T=-dt-1
        if event.type == KEYDOWN:
            if event.key == K_UP:
                origine[1]=origine[1]+10
            if event.key == K_DOWN:
                origine[1]=origine[1]-10
            if event.key == K_LEFT:
                origine[0]=origine[0]+10
            if event.key == K_RIGHT:
                origine[0]=origine[0]-10
            if event.key == K_o:
                origine=[650,400]
            if event.key == K_p:
                echelle*=2
            if event.key == K_m:
                echelle/=2
            if event.key == K_a:
                dt=dt*2
            if event.key == K_z:
                dt=dt/2
            if event.key == K_r:
                A=[10,[0,0],[0,0],[0,0]]
                B=[0.1,[1,0],[0,3],[0,0]]
                T=temps
                EppA=[epp(A,O)]
                EcA=[ec(A)]
                xt=[0]
                i=0
            if event.key == K_SPACE:
                dt,t0=t0,dt

    screen.fill("black")"""

    pfd(A,[forceG(A,O)])
    vitesse(A,dt)
    position(A,dt)

    EppA.append(epp(A,O))
    EcA.append(ec(A))
    xt.append(xt[i]+dt)
    i+=1

    """pygame.draw.circle(screen, "red",(echelle*O[1][0]+origine[0],origine[1]-echelle*O[1][1]), 5)
    pygame.draw.circle(screen, "green",(echelle*A[1][0]+origine[0],origine[1]-echelle*A[1][1]), 5)

    pygame.display.flip()
    clock.tick(1000000000)"""
    T-=dt
"""pygame.quit()"""

EmA=[EppA[i]+EcA[i] for i in range(len(EcA))]
deltaEm=[EmA[i]/EmA[0] for i in range(len(EmA))]

import matplotlib.pyplot as plt

if True:
# Tracé du graphe

    #plt.plot(xt, EmA, marker=',', linestyle='-', color='b', label='energie mecanique de A')
    plt.plot(xt, deltaEm, marker=',', linestyle='-', color='r', label='energie mecanique de A')
    plt.yscale('log')
    plt.ylim(0,10)


# Ajout des titres et légendes
    plt.title("frottements numerique ordre 1")
    plt.xlabel("t")
    plt.ylabel("Em")
    plt.legend()
    plt.grid(True)

# Affichage du graphe
    plt.show()
