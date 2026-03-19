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


#initialisation

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

    [5.972*10**24,[149597870700,0],[0,29.78*1000],[0,0]],  #terre
    [6.418*10**23,[-227940000000,0],[0,-24080],[0,0]],  #mars

    ]
    couleur=["cyan","yellow"]

    couleur0=["silver","pink","cyan","salmon","brown","tan","mediumpurple","slateblue"]


def initiaterepere():
    global origine,g,t,t0,T
    origine=[650,400]
    g=5*10**(-10)
    t=5000
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

def start():
    global origine
    global O,M,couleur,fusee,tpousse,fpoussee
    global g,t,t0,T

    initiaterepere()
    initiateplanete()
    initiatefusee()

    n=len(M)

    pygame.init()
    font = pygame.font.Font(None, 74)  # Police par défaut, taille 74
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Terrain de jeu/fleche/o/p/m/a/z/r")
    clock = pygame.time.Clock()
    running = True
    play=True
    poussee=False
    deltav=2952.3

    pause=1800

    C=[]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pause=0
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    origine[1]=origine[1]+10
                    screen.fill("black")
                if event.key == K_DOWN:
                    origine[1]=origine[1]-10
                    screen.fill("black")
                if event.key == K_LEFT:
                    origine[0]=origine[0]+10
                    screen.fill("black")
                if event.key == K_RIGHT:
                    origine[0]=origine[0]-10
                    screen.fill("black")
                if event.key == K_o:
                    origine=[650,400]
                    screen.fill("black")
                if event.key == K_p:
                    g=g*2
                    screen.fill("black")
                if event.key == K_m:
                    g=g/2
                    screen.fill("black")
                if event.key == K_a:
                    t=t*2
                if event.key == K_z:
                    t=t/2
                if event.key == K_r:
                    initiateplanete()
                    initiatefusee()
                    poussee=False
                    T=0
                    screen.fill("black")
                if event.key == K_SPACE:
                    t,t0=t0,t
                if event.key == K_l:
                    npoussee(deltav)
                    poussee=True
        screen.fill("black")
        pygame.draw.circle(screen, "black",(origine[0],origine[1]), 4)

        for i in range(n):
            pygame.draw.circle(screen, "black" ,(origine[0]+g*M[i][1][0],origine[1]-g*M[i][1][1]), 4)



        #pfd
        traj(O,t)
        trajM(M,t)

#ellipse de hohmann
        beta=angle2planetes(0,1)
        theta=math.pi-beta
        if (abs(theta-2.3372)<0.0001)and(poussee==False):
            npoussee(deltav)
            poussee=True
            print(theta)


        if poussee:
            pfd(fusee,[forceG(O,fusee)])
            vitesse(fusee,t)
            position(fusee,t)
        else:
            for i in range(1,3):
                for j in range(2):
                    fusee[i][j]=M[0][i][j]


#pygame

        pygame.draw.circle(screen, "red",(origine[0],origine[1]), 5)

        for i in range(n):
            pygame.draw.circle(screen, couleur[i] ,(origine[0]+g*M[i][1][0],origine[1]-g*M[i][1][1]), 5)
        pygame.draw.circle(screen, 'mediumpurple' ,(origine[0]+g*fusee[1][0],origine[1]-g*fusee[1][1]), 5)
        dist=distance(fusee,M[1])
        if dist<600000000:
            running=False
            screen.fill('black')
            text = font.render("bravo c'est gagne", True,'white')
            text_rect = text.get_rect(center=(origine[0],origine[1]))
            screen.blit(text, text_rect)





# Rendu du texte

        text = font.render(str((dist)//10000000*10000000),True , 'white')
        text0 = font.render(str(int(T))+'ans', True,'white')
        text_rect0 = text0.get_rect(center=(200, 250))
        text_rect = text.get_rect(center=(300, 150))
        screen.blit(text, text_rect)
        screen.blit(text0, text_rect0)
        """text = font.render(str(int(T))+'ans', True,'white')
        text_rect = text.get_rect(center=(200, 150))
        screen.blit(text, text_rect)"""


        pygame.display.flip()
        T+=t/31536000
        clock.tick(1000)  # limits FPS to t
    plt.pause(pause)
    pygame.quit()


def angle2planetes(indice1,indice2):
    normeSM=distance(O,M[indice1])
    normeST=distance(O,M[indice2])
    normeTM=distance(M[indice1],M[indice2])
    cos=(normeST**2+normeSM**2-normeTM**2)/(2*normeST*normeSM)
    return(math.acos(cos))


def distance(sys1,sys2):
    return(sqrt((sys1[1][0]-sys2[1][0])**2+(sys1[1][1]-sys2[1][1])**2))