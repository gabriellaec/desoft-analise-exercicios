def eh_primo(n):
    k = 0
    if n < 2 :
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i != 0:
                k += 1
        if k == (n-2) :
            return True
        else:
            return False
def primos_entre(a,b):
    lista = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            lista.append(i)
    return lista
                           
            
            