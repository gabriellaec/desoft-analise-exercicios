def verifica_quadrado_perfeito(n):
    impar=1
    while n>0:
        n-=impar
        impar+=2
    
    if n==0:
        return True
    else:
        return False