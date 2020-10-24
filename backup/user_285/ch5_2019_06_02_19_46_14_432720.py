def verifica_primo(n):
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
        else: 
            return True
def maior_primo_menor_que(n):
    if verifica_primo(n)==True:
        return n
    elif verifica_primo(n)==False:
        lista=[]
        for e in range(2,n,-1):
            if  n%e!=0:
            lista.append(e)
        return lista[-1]
    else:
        return -1