def verifica_quadrado_perfeito (x):
    n=x**2
    ímpar = 1
    i=0
    while i<ímpar:  
        n-=ímpar
        i+=1
        ímpar+=2
        if n==0:
            return True
        if n<0:
            return False