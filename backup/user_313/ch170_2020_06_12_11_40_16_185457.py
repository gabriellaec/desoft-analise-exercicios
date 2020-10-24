def apaga_repetidos(a):
    lista = list()
    for i in a:
        if i not in lista:
            lista.append(i)
            
        else:
            lista.append("*")
            
    x = ''.join(lista)
    return x