def junta_nome_sobrenome(lista_nome, lista_sobrenome):
    lista_nomesobrenome = []
    contador = 0
    while contador <= len(lista_nome)-1 and contador <= len(lista_sobrenome)-1:
        lista_nomesobrenome.append(lista_nome[contador]+" "+lista_sobrenome[contador])
        contador += 1
    return lista_nomesobrenome