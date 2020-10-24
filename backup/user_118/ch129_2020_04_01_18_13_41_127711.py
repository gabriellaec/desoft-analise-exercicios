def verifica_quadrado_perfeito (x):
    n=x**2
    ímpar=1
    i=0
    while i<n:  
        n-=ímpar
        ímpar+=2
        i+=1
        if x==0:
            return True
        if x<0:
            return False