def junta_nome_sobrenome (lista_nomes, lista_sobrenomes):
    i = 0
    lista_final = []
    while i < len(lista_nomes):
        lista_final.append(lista_nomes[i] + " " + lista_sobrenomes[i])
        i += 1
    return (lista_final) 