def verifica_primo(x):
    i=2
    while i<x:
        if x%i==0:
            return False
        i+=1
    return True
def maior_primo_menor_que(n):
    if n<2:
        return -1
    while verifica_primo(n)==False:
        n-=1
    return n   
        