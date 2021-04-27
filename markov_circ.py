import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.stats import cosine
matplotlib.use("Agg")
import matplotlib.animation as animation
import sys

def next_ang(angle,fun):
     return (angle + 2*fun)%(2*np.pi)

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
     '''
     n=607
     arr=[(2*k*np.pi)/n for k in range(n)]
     '''
     fig = plt.figure()
     circ.plot(markov[0],markov[1],'bs')
     while(0!=step):
          length = len(markov)
          chain.append(pos)
          fun=np.random.uniform(0,np.pi,1)
          #fun=ber(np.pi/2,2*(np.pi/3))
          #fun = ter(np.pi/4,5*np.pi/6,2*(np.pi/3))          
          #fun=arr[np.random.randint(0,n)]
          markov +=[r*np.cos(pos)]
          markov +=[r*np.sin(pos)]
          circ.plot(markov[length],markov[length+1],'bs')
          circ.plot([markov[length-2],markov[length]],[markov[length-1],markov[length+1]],color="steelblue")
          pos=np.degrees(next_ang(pos,fun))[0]          
          histo.hist(chain,stacked=True)
          plt.pause(1e-6)
          step -= 1
          histo.clear()
     print(chain)
     histo.hist(chain,stacked=True)
     plt.savefig(sys.argv[3])
     plt.show()

main()

'''
theta=np.arange(0,2*np.pi,0.01)
r=1
x=r*np.cos(theta)
y=r*np.sin(theta)
fig,(circ,histo) = plt.subplots(2,figsize=(8,8))
circ.set_aspect(1)
circ.set_title("Random walk on the boundary")
circ.plot(x,y,'red')
pos=np.pi/
circ.plot(np.cos(pos),np.sin(pos))
pos+=np.pi/2
'''
