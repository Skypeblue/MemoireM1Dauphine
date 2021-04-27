import numpy as np
from math import sqrt,floor
from matplotlib.collections import PatchCollection
from matplotlib.path import Path
import matplotlib.pyplot as plt
from functools import reduce
import operator as op
import matplotlib.patches as patches
import sys

def findFun(a,b):
    x_a=a[0]
    x_b=b[0]
    y_a=a[1]
    y_b=b[1]
    if(y_a==y_b):
        return (lambda x:y_a)
    elif(x_a==x_b):
        return True
    else:
        m=(y_b-y_a)/(x_b-x_a)
        p=y_a-m*x_a
        return (lambda x:m*x+p)

#vertices = [(1,0),(-1,2),(3,4),(4,0)]
vertices=[(1,0),(-3,3),(4,5),(8,3),(6,0)]


def createPath(vertices):
    codes=[Path.MOVETO]
    for i in range(len(vertices)-1):
        codes.append(Path.LINETO)
    vertices.append(vertices[0])
    codes.append(Path.CLOSEPOLY)
    return Path(vertices,codes)

path=createPath(vertices)

vertices.pop(len(vertices)-1)

def ineq(fun,boo):
    if boo:
        return lambda x,y: y>=round(fun(x),1)
    else:
        return lambda x,y: y<=round(fun(x),1)
'''
func=[]
con=[]

for i in range(4):
    f=findFun(vertices[i-2],vertices[i-1])
    func.append(f)

con.append(ineq(func[0],True))
con.append(ineq(func[1],True))
con.append(ineq(func[2],False))
con.append(ineq(func[3],False))

x=np.linspace(0,10,1000)
fig, ax = plt.subplots()
ax.set_xlim(0, 11)
ax.set_ylim(0, 11)
for f in func:
    plt.plot(x,f(x))

plt.plot(10,10,'bs')
'''

def condArray(vertices):
    cond=[]
    for i in range(len(vertices)):
        fun=findFun(vertices[-2+i],vertices[-1+i])
        boo=vertices[i][1]>=round(fun(vertices[i][0]),1)
        if boo:
            #cond.append(lambda x,y:y>=round(fun(x),1))
            cond.append(ineq(fun,boo))
        else:
            #cond.append(lambda x,y:y<=round(fun(x),1))
            cond.append(ineq(fun,boo))
    return cond

cond=condArray(vertices)

def isHere(p):
    return reduce(op.and_,list(map(lambda f:f(p[0],p[1]),cond)),True)

'''
a=4
b=4
print(list(map(lambda f:f(a,b),cond)))
print(isHere([a,b]))

'''
dis=lambda A,B:sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)
perim=lambda a:sum(list(map(lambda i: dis(a[i-1],a[i]),range(len(a)))))

per=perim(vertices)/2

def next(a,dist,tol=1e-5):
    theta=np.random.uniform(-np.pi/2,np.pi/2)
    r=.3
    start = [a[0],a[1]]
    if not isHere([a[0]+r*np.cos(theta),a[1]+r*np.sin(theta)]):
        theta += np.pi
    b=[a[0]+dist*np.cos(theta),a[1]+dist*np.sin(theta)]
    while dis(a,b)>tol :
        m=[(a[0]+b[0])/2,(a[1]+b[1])/2]
        if isHere(m):
            a=m
        else:
            b=m
    m=[(a[0]+b[0])/2,(a[1]+b[1])/2]
    return (m,np.linspace(start,m,floor(dis(start,m)/.01)+1))

def main():
    fig, (stoch,aimd) = plt.subplots(2,figsize=(8,8))
    patch = patches.PathPatch(path, facecolor='orange', lw=2)
    stoch.add_patch(patch)
    stoch.set_title("Stochastic billiard on a polygon")
    b=vertices[1]
    n=int(sys.argv[1])
    markov = [b[0]]
    markov += [b[1]]
    AIMD = [0]
    dist = 0
    process=[]
    while n!=0:
        stoch.plot(b[0],b[1],'bs')
        length = len(markov)
        ne = next(b,per)
        b = ne[0]
        process = ne[1]
        process[-1] = [markov[-2],markov[-1]]
        markov += [b[0]]
        markov += [b[1]]
        AIMD += list(map(lambda x:dis([markov[length-2],markov[length-1]],x),process))
        plt.pause(1e-8)
        stoch.plot([markov[length-2],markov[length]],[markov[length-1],markov[length+1]],color="steelblue")
        dist += dis([markov[length-2],markov[length-1]],[markov[length],markov[length+1]])
        n-=1
    aimd.set_title("AIMD process")
    x = np.linspace(0,len(AIMD)*.01+1,len(AIMD))
    aimd.plot(x,AIMD,color="steelblue")
    plt.show()
main()
