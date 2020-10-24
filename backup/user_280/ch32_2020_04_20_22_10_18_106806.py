def eh_primo (x):
    if x==2:
        return True
    elif x==0 or x==1:
        return False        
    elif x%2==0:
        return False
    else:
        n = 3
        while n < x:
            if x%n==0:
                return False
            n += 2
        return True

def lista_primos(n):
    lista = []
    i = 0
    while len(lista) < n+1:
        if eh_primo(i) == True:
            lista.append(i)
        i+=1
    return lista
        
    