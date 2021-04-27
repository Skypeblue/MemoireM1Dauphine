import numpy as np
import matplotlib.pyplot as plt
import sys

rate = 2
q = float(sys.argv[1])

dirac=lambda z:lambda:z
dira=dirac(q)
unif = lambda nb: np.random.uniform(size=nb)
    
def AIMD(nb,fun,step=.01,tol=1e-2):
    arrival = np.random.exponential(rate,nb)
    jump=np.cumsum(arrival)
    jump=np.insert(jump,0,0)
    AIMD=[]
    t=step
    aimd=0
    for i in range(nb-1):
        while np.abs(t-jump[i+1])>tol:
            AIMD += [aimd+t-jump[i]]        
            t += step
        aimd = fun()*(aimd+jump[i+1]-jump[i])    
        AIMD += [aimd]
    return [AIMD,t]

def main():
    nb=5
    fig, ax = plt.subplots()
    process=AIMD(nb,dira)    
    aimd=process[0]
    t=process[1]
    x=np.linspace(0,t,len(aimd))
    ax.set_xlabel("$t$")
    ax.set_ylabel("$X(t)$")
    ax.set_title("Process AIMD with $\delta_i$ = "+sys.argv[1])
    plt.plot(x,aimd,color="steelblue")
    plt.show()
        
main()
        
            
