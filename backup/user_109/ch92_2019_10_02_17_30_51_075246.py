def simplifica_dict(dicionario):
    lista = []
    for chave, valor in dicionario.items():
        if chave not in lista:
            lista.append(chave)
            if valor not in lista:
                lista.append(valor)

    return lista