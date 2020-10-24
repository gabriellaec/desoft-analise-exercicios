def junta_nome_sobrenome(lista1, lista2):
    y = []
    i = 0
    
    while i < len(lista1):
        x = lista1[i] + ' ' + lista2[i]
        i += 1
        y.append(x)
    return y