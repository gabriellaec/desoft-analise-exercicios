def eh_primo(n):
    if (n == 0) or (n == 1):
        return False
    elif n == 2:
        return True
    else:
        i = n-2
        if n % 2 == 0:
            return False
        while i>1:
            if n % i == 0:
                return False
            i -= 2
            if i == 0:
                return True
        return True
def lista_primos(n):
    lista = []
    a = 0
    while len(lista)<=n:
        if eh_primo(n[i]) == True:
            lista.append(n[i])
            return lista
    
    