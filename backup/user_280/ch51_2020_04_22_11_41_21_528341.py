def eh_primo (x):
    if x==2:
        return True
    elif x<2:
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

def primos_entre(a,b):
    lista = []
    i = a
    while i<=b:
        if eh_primo(i) == True:
            lista.append(i)
        i+=1
    return lista