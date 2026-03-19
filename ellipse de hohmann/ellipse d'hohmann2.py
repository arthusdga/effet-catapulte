
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

couleur=["cyan","yellow"]



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


def start():
    global origine
    global O,M,couleur,fusee,tpousse,fpoussee
    global g,t,t0,T

    Lt5000=[(2.3865, 0.7672184170472586), (2.3743, 0.7583396752918031), (2.3373, 0.6435502283105577)]
    L=Lt5000

    theta=math.pi-2.367635518
    theta=math.pi-L[0][0]

    initiaterepere()
    O,M=initiateplanete(theta)
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
    deltavA=2952.332061
    deltavB=2655.767751
    transitoire=True

    pause=20

    C=[]
    #t=100
    npoussee(deltavA)
    repetition=0
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
                    O,M=initiateplanete(theta)
                    initiatefusee()
                    npoussee(deltavA)
                    T=0
                    screen.fill("black")
                if event.key == K_SPACE:
                    t,t0=t0,t
                if event.key == K_l:
                    npoussee(deltavA)
                    poussee=True
                if event.key == K_v:
                    t=-t

        if repetition%100==0:
            """pygame.draw.circle(screen, "black",(origine[0],origine[1]), 4)
            for i in range(n):
                pygame.draw.circle(screen, "black" ,(origine[0]+g*M[i][1][0],origine[1]-g*M[i][1][1]), 4)"""
            screen.fill("black")



        #pfd
        trajM(M,t)
        traj(fusee,t)




#pygame
        if repetition%100==0:
            pygame.draw.circle(screen, "red",(origine[0],origine[1]), 4)

            for i in range(n):
                pygame.draw.circle(screen, couleur[i] ,(origine[0]+g*M[i][1][0],origine[1]-g*M[i][1][1]), 4)
            pygame.draw.circle(screen, 'mediumpurple' ,(origine[0]+g*fusee[1][0],origine[1]-g*fusee[1][1]), 2)

        if distance(fusee,M[1])<600000000 and transitoire:
            npoussee(deltavB)
            transitoire=False
            #running=False
            #screen.fill('black')
            #text = font.render("bravo c'est gagne", True,'white')
            #text_rect = text.get_rect(center=(origine[0],origine[1]))
            #screen.blit(text, text_rect)





# Rendu du texte
        rect = pygame.Rect((0,0),(100,100))
        text = font.render(str(int(T))+'jours', True,'white')
        text_rect = text.get_rect(center=(200, 150))
        screen.blit(text, text_rect)

        if repetition%100==0:
            pygame.display.flip()
            clock.tick(1000)  # limits FPS to t
        T+=t/31536000*365
        repetition+=1

    plt.pause(pause)
    pygame.quit()
