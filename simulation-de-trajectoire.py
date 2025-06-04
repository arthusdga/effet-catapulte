from math import sqrt
#on definit un corps par sa masse, sa position, sa vitesse, et son acceleration

#a l'instant initial on initialise l'acceleration(qu'on veut calculer) a 0



def forceG(A,B):
    r=0
    for i in range(3):
        r+=(A[1][i]-B[1][i])**2
    r=sqrt(r)
    ur=[]
    for i in range(3):
        ur.append((B[1][i]-A[1][i])/r)
    F=[]
    for i in range(3):
        F.append((-6.67*10**(-11)*A[0]*B[0]/r**2)*ur[i])
    return F

def pfd(systeme,listeF):
    sommeF=[0,0,0]
    for i in range(len(listeF)):
        for j in range(3):
            sommeF[j]+=listeF[i][j]
    for i in range(3):
        systeme[3][i]=sommeF[i]/systeme[0]

def vitesse(systeme,dt=1):
    for i in range(3):
        systeme[2][i]=systeme[3][i]*dt

def position(systeme,dt=1):
    for i in range(3):
        systeme[1][i]=systeme[2][i]*dt


#console
O=[100,[0,0,0],[0,0,0],[0,0,0]]
M=[ 10,[1,0,0],[0,1,0],[0,0,0]]
Fm=forceG(O,M)
Fo=forceG(M,O)
pfd(M,[Fm])
pfd(O,[Fo])
print(M)
print(O)



