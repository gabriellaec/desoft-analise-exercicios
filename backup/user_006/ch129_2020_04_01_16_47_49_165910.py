def verifica_quadrado_perfeito(n):
    i=0
    while n>0:
        n=n-(1+2*i)
        i=i+1
    if n==0: 
        return True
    else:
        return False
    
    