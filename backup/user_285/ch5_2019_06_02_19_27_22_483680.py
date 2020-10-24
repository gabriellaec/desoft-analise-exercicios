def verifica_primo(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i!=0:
            return True
        else: 
            return False
def maior_primo_menor_que(n):
    if verifica_primo(n)==True:
        return n
    else:
        return -1