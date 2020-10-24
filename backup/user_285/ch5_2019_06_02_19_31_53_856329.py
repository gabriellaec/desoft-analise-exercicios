def verifica_primo(n):
    for i in range(3,n):
        if n%i!=0:
            return True
        else: 
            return False
def maior_primo_menor_que(n):
    if verifica_primo(n)==True:
        return n
    elif verifica_primo(n)== False:
        k=0
        for e in range(3,n):
    else:
        return -1