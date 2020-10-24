def lista_primos (n):
    lista = []
    if n == 2:
        lista.append(n)
    elif n == 0 or n ==1 or n %2 == 0:
        del [n]
    i = 3
    while i < n:
        if n %i == 0:
            del [n]
        else:
            i += 2
            lista.append (n) 
    return lista