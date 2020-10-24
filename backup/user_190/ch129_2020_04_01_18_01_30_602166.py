def verifica_quadrado_perfeito(n):
    n=int(input('numero a ser verificado: '))
    impar=1
    i=0
    while i<n:
        n-=impar
        impar+=2
        i+=1
        if n==0:
            return True
        elif n<0:
            return False