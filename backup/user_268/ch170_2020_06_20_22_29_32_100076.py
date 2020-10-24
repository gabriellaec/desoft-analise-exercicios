def apaga_repetidos(st):
    lit = []
    lista = []
    
    for i in range(len(st)):
        lista.append(st[i])
        if st[i] in lit:
            lista[i] = '*'
            print(lista)
        else:
            lit.append(st[i])
            print(lit)
    retorno = ''.join(lista)
            
    return retorno
        