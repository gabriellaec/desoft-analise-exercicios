def separa_trios (lista_nomes):
    i=0
    while i< len(lista_nomes):
        novo_trio = lista_nomes[i:i+3]
        i+= 3
    return novo_trio