def junta_nome_sobrenome (lista_nomes, lista_sobrenomes):
    var = 0
    lista_final = []
    while var != len(lista_nomes):
        lista_final.append(lista_nomes[var] + ' ' + lista_sobrenomes[var])
        var += 1

    return lista_final