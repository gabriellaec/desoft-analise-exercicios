def junta_nome_sobrenome(lista_nomes, lista_sobrenomes):
    lista_nomes_completos = []
    i = 0
    while (i < len(lista_nomes)):
        nome_completo = lista_nomes[i] + " " + lista_sobrenomes[i]
        lista_nomes_completos.append(nome_completo)
        i = i + 1

    return lista_nomes_completos