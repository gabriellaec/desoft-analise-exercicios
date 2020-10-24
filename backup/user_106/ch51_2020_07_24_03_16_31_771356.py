def eh_primo(n):
    if n < 2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        i=3
        while i<n:
            if n%i==0:
                return False
            i+=2
        return True

def primos_entre(a, b):
    lista_p = []
    for i in range(a, b+1):
        if eh_primo(i):
            lista_p.append(i)
    return lista_p