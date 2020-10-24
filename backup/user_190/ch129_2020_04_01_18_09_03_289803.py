def verifica_quadrado_perfeito(n):
    x=n**2
    impar=1
    i=0
    while i<x:
        n-=impar
        impar+=2
        i+=1
        if n==0:
            return True
        elif n<0:
            return False