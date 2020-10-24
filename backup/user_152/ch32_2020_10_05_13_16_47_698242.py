def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
         return True    
    elif n%2 == 0:
         return False
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            return True
        else:
            return False
        
def lista_primos(x):
    lista = []
    i = 1
    while len(lista) < x:
        if eh_primo(i) == True:
            lista.append(i)
        i += 1
    return lista