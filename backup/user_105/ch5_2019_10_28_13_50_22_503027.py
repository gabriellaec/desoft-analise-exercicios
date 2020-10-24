def eh_primo (x):
    if x==2:
        return True
    elif x==1 or x==0:
        return False
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n=n+2
        else: 
            return True
def maior_primo_menor_que(j):
    lista = []
    for z in range(j+1):
        if eh_primo(z)==True:
            lista.append(z)
    if len(lista)==0:
        return -1
    else:
        return lista[-1]
        
        

    