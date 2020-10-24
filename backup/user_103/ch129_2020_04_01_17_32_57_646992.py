def verifica_quadrado_perfeito(n):
    a=1
    if n==1:
        return True
    while a<=n:
        n-=a
        if n==0:
            return True 
        elif n<0:
            return False
        i+=2