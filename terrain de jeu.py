#terrain de jeu

import pygame
import random
from math import sqrt
import math
import numpy as np

from pygame.locals import *

##forcee


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


## trajectoire

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
    pfd(systeme,force(M))
    vitesse(systeme,t)
    position(systeme,t)

def trajM(planetes,t):
    n=len(planetes)
    F=nforces(planetes)
    for i in range(n):
        pfd(planetes[i],F[i])
        vitesse(planetes[i],t)
        position(planetes[i],t)


##initialisation

#fonction de recuperation des differentes positions, vitesses, et acceleration des planetes,(et masses) sur internet

origine=[]
g=0
t=0
t0=0
T=0
O=[]
M=[]
couleur=[]
couleur0=[]



def initiateplanete():
    global O,M,couleur,couleur0
    O=[2*10**30,[0,0],[0,0],[0,0]]
    M=[
    [3.301*10**23,[46001200,0],[0,58980],[0,0]],  #mercure
    [4.8675*10**24,[108209500000,0],[0,35025.71],[0,0]],  #venus
    [5.972*10**24,[149597870700,0],[0,29.78*1000],[0,0]],  #terre
    [6.418*10**23,[227940000000,0],[0,24080],[0,0]],  #mars
    [1.8986*10**27,[778300000000,0],[0,13714],[0,0]],  #jupiter
    [5.6846*10**26,[14289700000000,0],[0,9640.7],[0,0]],  #saturne
    [8.681*10**25,[2870700000000,0],[0,6796.732],[0,0]],  #uranus
    [1.0243*10**26,[4498400000000,0],[0,5432.48],[0,0]],  #neptune
    ]
    couleur=["green","green","cyan","green","green","green","green","green"]

    couleur0=["silver","pink","cyan","salmon","brown","tan","mediumpurple","slateblue"]


def initiaterepere():
    global origine,g,t,t0,T
    origine=[650,400]
    g=5*10**(-11)
    t=5000
    t0=0           #sert pour stopper le temps
    T=0


##fusee

#on prends l'exemple de le fusee ariane : poids fusee=270 000kg
#                                         carburant=480 000kg

fusee=[]
tpoussee=0
fpoussee=0

def initiatefusee():
    global fusee,tpousse,fpoussee
    fusee=[750000,[227940000000,0],[0,24080],[0,0]]
    tpoussee=0
    fpoussee=0

def npoussee(deltav):                     #norme de la pousse uniquement
    global fpoussee,t
    fpoussee=fusee[0]*deltav/t

#on va lui donner du carburant. il faut set une quantite de carburant maximale et le poids a vide, modifier sa masse en fonction de la pousse

#objectif 1: ellipse de Hohmann pour aller sur mars

#objectif 2: quitter le plus vite possible en dehors du systeme solaire, regarder les accelerations subies (4-6g max)

# rajouter une variable qui calcule le temps de trajet



## controle

def start():
    global origine
    global O,M,couleur,fusee,tpousse,fpoussee
    global g,t,t0,T

    initiaterepere()
    initiateplanete()
    initiatefusee()

    tpoussee=0

    n=len(M)

    pygame.init()
    font = pygame.font.Font(None, 74)  # Police par défaut, taille 74
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Terrain de jeu/fleche/o/p/m/a/z/r")
    clock = pygame.time.Clock()
    running = True
    play=True

    C=[]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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
                    g=g*5
                if event.key == K_m:
                    g=g/5
                if event.key == K_a:
                    t=t*2
                if event.key == K_z:
                    t=t/2
                if event.key == K_r:
                    initiateplanete()
                    initiatefusee()
                    T=0
                if event.key == K_SPACE:
                    t,t0=t0,t
        screen.fill("black")


        #pfd
        traj(O,t)
        trajM(M,t)

#ellipse de hohmann
        if tpoussee==0:
            fusee[1:4]=M[3][1:4]

        beta=angle2planetes(4,3)


        if (beta==2.14016189*10**(-10))and (tpoussee==0):
            energiemeca=(-6.67*(10**(-11))*2*(10**30)*fusee[0]/(2*(227940000000+778300000000)))
            deltavA=sqrt(2*energiemeca/fusee[0]-2*(10**30)*6.67*10**(-11)/227940000000)-24191.76989
            tpoussee+=t
            npousse(deltavA)

        if tpoussee>0:
            npousse+=t
            traj(fusee,t)


        if tpoussee>549103636:
            deltat,tpousset=tpoussee,-1
            deltavB=13091.95186-sqrt(2*energiemeca/fusee[0]-2*(10**30)*6.67*10**(-11)/778300000000)
            npousse(deltavB)

#pygame

        pygame.draw.circle(screen, "red",(origine[0],origine[1]), 4)
        pygame.draw.circle(screen, 'mediumpurple' ,(origine[0]+g*fusee[1][0],origine[1]-g*fusee[1][1]), 3)
        for i in range(n):
            pygame.draw.circle(screen, couleur[i] ,(origine[0]+g*M[i][1][0],origine[1]-g*M[i][1][1]), 2)





# Rendu du texte
        text = font.render(str(int(T))+'ans', True,'white')
        text_rect = text.get_rect(center=(200, 150))
        screen.blit(text, text_rect)


        pygame.display.flip()
        T+=t/31536000
        clock.tick(1000)  # limits FPS to t
    pygame.quit()


def angle2planetes(indice1,indice2):
    SM=[M[indice1][1][0]-O[1][0],M[indice1][1][1]-O[1][1]]
    ST=[M[indice2][1][0]-O[1][0],M[indice2][1][1]-O[1][1]]
    TM=[M[indice2][1][0]-M[indice1][1][0],M[indice2][1][1]-M[indice1][1][1]]
    normeSM=sqrt(SM[0]**2+SM[1]**2)
    normeST=sqrt(ST[0]**2+ST[1]**2)
    normeTM=sqrt(TM[0]**2+TM[1]**2)
    cos=(normeST**2+normeSM**2-normeTM**2)/(2*normeST*normeSM)
    return(math.acos(cos))

"""probleme avec le soleil je n'arrive pas a bien l'afficher(autre qu'en ne le faisant pas bouger de la position d'origine)
+probleme de mercure que je n'arrive pas a modeliser
+meme probleme pour pluton"""

##a faire une fois le code finis

#stopper quand on quitte le systeme solaire et renvoyer alors la vitesse de la fusee (sphere de hill, 1~2*94608*10**11m)

#entre chaque changement de trajectoire faire un graphe sur lequel on implente les differentes energies

# apres avoir fait le trajet de la fusee, il faudra tracer la courbe de variation des energies cinetiques, potentielle (effectif et reel), et mecanique de la fusee
