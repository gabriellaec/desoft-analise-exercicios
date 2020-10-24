def interseccao_chaves(dicionario1, dicionario2):
    lista = []
    for chave1, valor1 in dicionario1.items():
        for chave2, valor2 in dicionario2.items():
            if chave1 == chave2:
                lista.append(chave1)

    return lista