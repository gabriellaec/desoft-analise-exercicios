def verifica_quadrado_perfeito(n):
    i=0
    while n>i:
        n=n-(2*i+1)
        i+=1
    if n==0:
        return True
    else:
        return False