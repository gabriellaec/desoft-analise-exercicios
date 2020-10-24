def verifica_primo(n):
    if n==2:
        return True
    contador=0
    for i in range(1,n):
        if n%i==0:
            contador+=1
            if contador>1:
                return True
        else: 
            return False
def maior_primo_menor_que(n):
    if verifica_primo(n)==True:
        return n
    elif verifica_primo(n)==False:
        lista=[]
        for e in range(2,n):
            if  n%e!=0:
                lista.append(e)
        return lista[-1]
    else:
        return -1