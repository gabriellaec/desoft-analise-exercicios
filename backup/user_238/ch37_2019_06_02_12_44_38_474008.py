def primo(p):
    if p > 1:
        for x in range (2,p):
            if p%x == 0:
                return False
    else:
        return False
    return True


def lista_primos(n):
    lista=[]
    i=0

    while len(lista) < n:
        primos=primo(i)
        if primos:
                lista.append(i)
        i+=1
    return lista
        