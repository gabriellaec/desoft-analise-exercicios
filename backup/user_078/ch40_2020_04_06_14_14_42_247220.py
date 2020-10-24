def soma_valores(lista):
    i=0
    s=lista[i]
    for i in range (0, len(lista)):
        s+=s[i]
    return s
        