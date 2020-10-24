def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range (3, n, 2):
        if (n%2==0):
            return False 
        elif(n%i == 0):
            return False
    else:
        return True

def lista_primos(n):
    lista = []
    j = 0
    while n > len(lista):
        if eh_primo(j) == True:
            lista.append(j)
        j = j + 1
    return lista