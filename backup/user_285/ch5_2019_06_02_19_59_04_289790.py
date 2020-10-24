def verifica_primo(n):
    if n==2:
        return True
    contador=0
    for i in range(2,n):
        if n%i==0:
            contador+=1
            if contador>1:
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