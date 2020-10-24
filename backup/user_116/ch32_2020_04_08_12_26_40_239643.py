def eh_primo (n):
    if n == 2:
        return True
    elif n == 0 or n == 1:
        return False
    elif n%2 == 0:
        return False
    else:
        contador = 3
        while contador < n:
            if n%contador == 0:
                return False
            contador += 2    
        return True
   

def lista_primos(q):
    i=0
    lista=[]
    while len(lista)<q:
        if eh_primo(i)==True:
            lista.append(i)
            i+=1
        else:
            i+=1
    return lista