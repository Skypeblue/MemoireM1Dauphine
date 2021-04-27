import numpy as np
from math import sqrt,floor
import matplotlib.pyplot as plt
from functools import reduce
import sys
import matplotlib.pyplot as plt

nb = 4

def next_ang(angle,fun):
     return float((angle + 2*fun)%(2*np.pi))

def ber(x,y):
     return (x if np.random.binomial(1,.5) else y)

def ter(x,y,z):
     rand=np.random.randint(0,3)
     if rand==0:
          return x
     elif rand==1:
          return y
     else:
          return z

def unif(arr):
     rand=np.random.randint(0,len(arr))
     return arr[rand]

dis=lambda A,B:sqrt((B[0]-A[0])**2+(B[1]-A[1])**2)

def findFun(angle):
    y = np.sin(angle)
    x = np.cos(angle)
    return (lambda z: (y/x)*z)
def ineq(fun1,fun2,boo,dir=True,val=3):
    if dir:
        if boo:
            return lambda x,y: y>=fun1(x) and y<fun2(x)
        else:
            return lambda x,y: y<=fun1(x) and y>fun2(x)
    else:
        if boo:
            return lambda x,y: y>=fun1(x) and y>fun2(x)
        else:
            return lambda x,y: y<=fun1(x) and y<fun2(x)

def slice(nb):
    angle = np.linspace(0,np.pi,nb,endpoint=False)+np.radians(20)    
    fun = list(map(findFun,angle))
    zone = []
    for i in range(nb):
        if np.pi/2>=angle[i-1] and np.pi/2<=angle[i]:
            zone.append(ineq(fun[i-1],fun[i],True,False))
            zone.append(ineq(fun[i-1],fun[i],False,False))
        else:
            zone.append(ineq(fun[i-1],fun[i],True))
            zone.append(ineq(fun[i-1],fun[i],False))
    return list(zone)

zone = slice(nb)
def ind(point):
     return [i for i in range(len(zone)) if zone[i](point[0],point[1])].pop()

def main():
     theta=np.arange(0,2*np.pi,0.01)
     r=1
     x=r*np.cos(theta)
     y=r*np.sin(theta)
     fig,(circ,histo) = plt.subplots(2,figsize=(8,8))
     circ.set_aspect(1)
     circ.set_title("Random walk on the boundary")
     circ.plot(x,y,'red')
     step=int(sys.argv[1])
     pos=np.radians(int(sys.argv[2]))
     markov =[r*np.cos(pos)]
     markov +=[r*np.sin(pos)]
     chain=[]
     #arr=[(2*k*np.pi)/n for k in range(n)]
     circ.plot(markov[0],markov[1],'bs')
     cont = []
     conte = []
     zoned = [0 for i in range(len(zone))]     
     while 0!=step :
          length = len(markov)
          chain.append(np.degrees(pos))
          fun=np.random.uniform(0,np.pi,1)
          #fun=ber(np.pi/2,2*(np.pi/3))
          #fun = ter(np.pi/4,5*np.pi/6,2*(np.pi/3))
          #fun=arr[np.random.randint(0,n)]
          pos=next_ang(pos,fun)
          markov.append(r*np.cos(pos))
          markov +=[r*np.sin(pos)]
          circ.plot(markov[length],markov[length+1],'bs')
          start = [markov[length-2],markov[length-1]]
          end = [markov[length],markov[length+1]]
          cont = np.linspace(start,end,floor(dis(start,end)/.01)+1,endpoint=False)
          conte += [ind(point) for point in cont]              
          circ.plot([start[0],end[0]],[start[1],end[1]],color="steelblue")                   
          histo.hist(chain,stacked=True)
          plt.pause(1e-5)
          step -= 1
          histo.clear()          
     histo.hist(conte,bins=8)
     print([conte.count(i) for i in range(8)])
     plt.savefig(sys.argv[3])
     plt.show()
main()
