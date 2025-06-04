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

def vitesse(systeme,dt=0.01):
    for i in range(2):
        systeme[2][i]+=systeme[3][i]*dt

def position(systeme,dt=0.01):
    for i in range(2):
        systeme[1][i]+=systeme[2][i]*dt

#pour l'instant a defaut de mieux j'ai pris le module python car j'avais du mal a me rendre compte si mon code marchait
import turtle as t
m=t.Turtle()
o=t.Turtle()
t.reset
m.shape("circle")
o.shape("circle")
m.speed(500)
o.speed(500)

#console

O=[10**10,[0,0],[0,0],[0,0]]
M=[ 10,[1,0],[0,1],[0,0]]

m.goto(100*M[1][0],100*M[1][1])
o.goto(100*O[1][0],100*O[1][1])

def start():
    while True:
        Fm=forceG(O,M)
        Fo=forceG(M,O)
        pfd(M,[Fm])
        pfd(O,[Fo])
        vitesse(M)
        vitesse(O)
        position(M)
        position(O)
        m.goto(100*M[1][0],100*M[1][1])
        o.goto(100*O[1][0],100*O[1][1])
start()

#on voit un petit peu le debut de frottements numerique

t.mainloop()



