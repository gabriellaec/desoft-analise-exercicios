def verifica_primo(n):
    num=3
    while num<n:
        if n%2==0 or n%num==0:
            return False
        num+=2
    if n==0 or n==1:
        return False
    
    else:
        return True
def maior_primo_menor_que(n):
    if verifica_primo(n)==True:
        return n
    elif verifica_primo(n)==False:
        lista=[]
        for e in range(2,n):
            for k in range(2,e):
                if e%k!=0:
                    lista.append(e)
        return lista[-1]
    else:
        return -1