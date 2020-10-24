from math import factorial
import numpy as np  
def calcula_euler(x, n):
    lista=np.arrange(2,n,1)
    i=0
    lista_nova=[]
    e=1+x
    while i<len(lista):
        lista_nova.append((x**lista[i])/factorial(lista[i]))
        i+=1
    i=0
    while i<len(lista_nova):
        e=e+lista_nova[i]
        i+=1
    e=e**(1/x)
    return e