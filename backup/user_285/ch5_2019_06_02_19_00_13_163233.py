def verifica_primo(n):
    for i in range(1,n):
        if n%i!=0:
            return True
        else: 
            return False
def maior_primo_menor_que(n):
    if verifica_primo(n)==True:
        return n
    elif verifica_primo(n)==False:
        for i in range(1,n,-1):
            if n%i!=0:
                return i
    else:
        return -1
            