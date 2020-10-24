# Define função pedida
def interseccao_chaves(dicionario1, dicionario2):
    lista_interseccoes = []
    # Verifica cada chave do dicionário 1
    for chave1 in dicionario1.keys():
        # Verifica e compara cada chave 2 com a chave 1 anterior
        for chave2 in dicionario2.keys():
            if chave2 == chave1:
                lista_interseccoes.append(chave1)
    return lista_interseccoes