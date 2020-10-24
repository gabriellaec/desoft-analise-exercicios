def subtracao_de_listas(lista1, lista2): 
    b = []
    i=0
    a=0
    while i < len(lista1):
        adicionar = True
        while a < len(lista2):
            if lista1[i] == lista2[a]:
                adicionar = False
            a += 1
        if adicionar:
            b.append(lista1[i])
            
        i += 1
    return b