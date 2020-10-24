def junta_nome_sobrenome(l1,l2):
    a = len(l1)
    contador = 0 
    novaLista = [0]*a

    while contador != a:
        novaLista[contador]= " ".join((l1[contador],l2[contador]))

        contador = contador + 1

    return novaLista