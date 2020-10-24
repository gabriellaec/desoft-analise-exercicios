def junta_nome_sobrenome(lista1, lista2):
    If = [0]*len(lista1)
    i = 0
    while i<len(lista1):
        If[i] = ('{} {}'.format(lista1[i], lista2[i]))
        i+=1
    return If