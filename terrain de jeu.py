#terrain de jeu

import pygame
import random
from math import sqrt
import math

from pygame.locals import *

##

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

##planetes

#fonction de recuperation des differentes positions, vitesses, et acceleration des planetes,(et masses) sur internet

g=5*10**(-11)
origine=[650,400]


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



##fusee

fusee=[100000,[],[],[]]

def poussee():
    pass

#on va lui donner du carburant. il faut set une quantite de carburant maximale et le poids a vide, modifier sa masse en fonction de la pousse

#objectif 1: ellipse de Hohmann pour aller sur mars

#objectif 2: quitter le plus vite possible en dehors du systeme solaire, regarder les accelerations subies (4-6g max)

# rajouter une variable qui calcule le temps de trajet


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

def forceO(M):
    n=len(M)
    FO=[]
    for i in range(n):
        FO.append(forceG(M[i],O))
    return(FO)

## controle

def start():
    global M
    n=len(M)
    global origine
    global g
    pygame.init()
    font = pygame.font.Font(None, 74)  # Police par défaut, taille 74
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Terrain de jeu/fleche/o/p/m/a/z/r")
    clock = pygame.time.Clock()
    O=[10**10,[0,0],[0,0] ,[0,0]]
    running = True
    play=True
    t=20000
    t0=0           #sert pour stopper le temps
    T=0
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
                    T=0
                if event.key == K_SPACE:
                    t,t0=t0,t
        screen.fill("black")
    #force
        F=nforces(M)
        #pfd
        pfd(O,forceO(M))
        vitesse(O)
        position(O)
        pygame.draw.circle(screen, "red",(origine[0],origine[1]), 4)
        for i in range(n):
            pfd(M[i],F[i])
            vitesse(M[i],t)
            position(M[i],t)
            pygame.draw.circle(screen, "green",(origine[0]+g*M[i][1][0],origine[1]-g*M[i][1][1]), 1.5)


# Rendu du texte
        text = font.render(str(int(T))+'ans', True,'white')
        text_rect = text.get_rect(center=(200, 150))
        screen.blit(text, text_rect)


        pygame.display.flip()

        T+=t/31536000
        clock.tick(1000)  # limits FPS to t
    pygame.quit()




"""probleme avec le soleil je n'arrive pas a bien l'afficher(autre qu'en ne le faisant pas bouger de la position d'origine)
+probleme de mercure que je n'arrive pas a modeliser
+meme probleme pour pluton"""

##a faire une fois le code finis

#stopper quand on quitte le systeme solaire et renvoyer alors la vitesse de la fusee (sphere de hill, 1~2*94608*10**11m)

#entre chaque changement de trajectoire faire un graphe sur lequel on implente les differentes energies

# apres avoir fait le trajet de la fusee, il faudra tracer la courbe de variation des energies cinetiques, potentielle (effectif et reel), et mecanique de la fusee
