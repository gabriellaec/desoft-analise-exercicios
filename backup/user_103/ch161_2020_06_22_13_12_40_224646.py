'''import math
def PiWallis(n):
    i=1
    j=1
    mult=1
    div= 1
    lista=[]
    while i < n:
        mult*=(2*i)
        div*=((2*i)-1) 
        a= mult/div
        lista.append(a)
    while j < n:
        mult2*=(2*i)
        div2*= ((2*i)+1)
        b= mul2/div2
        lista.append(b)
    resultado = math.prod(lista)
    return resultado'''

import math
def PiWallis(n):
    i=1
    j=1
    mult=1
    div= 1
    mult2=1
    div2= 1
    lista=[]
    while i < n:
        mult*=(2*i)
        div*=((2*i)-1) 
        a= mult/div
        lista.append(a)
        i+=1
    while j < n:
        mult2*=(2*i)
        div2*= ((2*i)+1)
        b= mult2/div2
        lista.append(b)
        j+=1
    print(lista)    
    resultado = math.prod(lista)
    return resultado

                    
        
        
    