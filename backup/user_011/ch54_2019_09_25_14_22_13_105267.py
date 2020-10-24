def junta_nome_sobrenome(lista1, lista2):
    l_nome_sobre = []
    i = 0
    while i < len(lista1):
        a = lista1[i] + " " + lista2[i]
        l_nome_sobre.append(a)
        i+=1
    return l_nome_sobre