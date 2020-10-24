def verifica_quadrado_perfeito(x):
    i=1
    while x>=i:
        x-=i
        i+=2
    if x<0:
        return False
    if x==0:
        return True