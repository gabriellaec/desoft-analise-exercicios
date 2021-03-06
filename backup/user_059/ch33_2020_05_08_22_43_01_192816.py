import matplotlib.pyplot as plt
import numpy

def eh_primo(x):
    if x<2:
        return False
    elif x==2:
        return True
    else:
        if x%2==0: 
            return False
        else:
            i = 3
            while i<x:
                if x%i == 0:
                    break
                i+=1
            if i==x:
                return True
            else:
                return False 
            
def primos_entre(a, b):
    cont = 0 
    i = b
    while i>=a:
        w = eh_primo(i)
        if w == True:
            cont +=1
        i = i-1
    return cont

tempo = np.arange(0,10,1)
plt.plot(tempo, primos_entre(10))
plt.show()