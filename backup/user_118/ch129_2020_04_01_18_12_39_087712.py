def verifica_quadrado_perfeito (x):
    n=x**2
    ímpar=1
    i=0
    while i<x:  
        n-=ímpar
        ímpar+=2
        i+=1
        if n==0:
            return True
        if n<0:
            return False