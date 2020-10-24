def interseccao_chaves (dicionario_1, dicionario_2):
    # Cria a lista onde serão adicionadas as chaves
    lista = []
    # Condição
    for k in dicionario_1.keys():
        # Verifica se a chave do dicionário 1 está no 2
        if k in dicionario_2.keys():
            # se sim, adiciona a chave à lista
            lista.append(k)
    return lista