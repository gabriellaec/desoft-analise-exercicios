def verifica_quadrado_perfeito(n):
    i=0
    while i>0:
        a=n-(2*i+1)
        i+=1
    if a==0 or n==1:
        return True
    else:
        return False