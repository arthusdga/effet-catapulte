from math import sqrt
#on definit un corps par sa masse, sa position, sa vitesse, et son acceleration

#a l'instant initial on initialise l'acceleration(qu'on veut calculer) a 0

#pour l'instant on fonctionnera en 2d


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

def vitesse(systeme,dt=10000):
    for i in range(2):
        systeme[2][i]+=systeme[3][i]*dt

def position(systeme,dt=10000):
    for i in range(2):
        systeme[1][i]+=systeme[2][i]*dt

#pour l'instant a defaut de mieux j'ai pris le module python car j'avais du mal a me rendre compte si mon code marchait
import turtle as t
m=t.Turtle()
o=t.Turtle()
b=t.Turtle()
t.reset
m.shape("circle")
o.shape("circle")
b.shape("circle")
m.speed(500)
o.speed(500)
b.speed(500)

#console
#grossissement
g=10**(-9)

O=[2*10**30,[0,0],[0,0],[0,0]]
M=[5.972*10**24,[149597870700,0],[0,29.78*1000],[0,0]]
B=[7.5*10**22,[384400*1000+149597870700,0],[0,29.78*1000+1020],[0,0]]

m.up()
o.up()
b.up()
m.goto(g*M[1][0],g*M[1][1])
o.goto(g*O[1][0],g*O[1][1])
b.goto(g*B[1][0],g*B[1][1])
m.down()
o.down()
b.down()

m.color("blue")
o.color("red")
b.color("green")

def start():
    while True:
        #force
        Fom=forceG(O,M)
        Fmo=forceG(M,O)
        Fob=forceG(O,B)
        Fbo=forceG(B,O)
        Fmb=forceG(M,B)
        Fbm=forceG(B,M)
        #pfd
        pfd(M,[Fom,Fbm])
        pfd(O,[Fmo,Fbo])
        pfd(B,[Fob,Fmb])
        vitesse(M)
        vitesse(O)
        vitesse(B)
        position(M)
        position(O)
        position(B)
        m.goto(g*M[1][0],g*M[1][1])
        o.goto(g*O[1][0],g*O[1][1])
        b.goto(g*B[1][0],g*B[1][1])
start()

#on voit un petit peu le debut de frottements numerique

#soleil=[2*10**30,[0,0],[0,0],[0,0]]
#terre=[5.972*10**24,[149597870700,0],[0,29.78*1000],[0,0]]
#lune=[7.5*10**22,[384400*1000+149597870700,0],[0,29.78*1000+1020],[0,0]]

#exemple2
"""O=[10**10,[1/2, sqrt(3)/2],[-sqrt(3)/3,1/3] ,[0,0]]
M=[10**10,[1/2,-sqrt(3)/2],[sqrt(3)/3,1/3]  ,[0,0]]
B=[10**10,[-1,0]          ,[0,-2/3]         ,[0,0]]"""

t.mainloop()

import matplotlib.pyplot as plt
import numpy as np

def graph(f,var1,var2,T=1000):
    X=[]
    Y=[]
    for i in range(0):
        pass


