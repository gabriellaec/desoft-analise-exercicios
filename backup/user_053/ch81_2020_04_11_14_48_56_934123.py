# Define função pedida
def interseccao_valores(dicionario1, dicionario2):
    lista_interseccoes = []
    # Percorre valores do dicionário 1
    for valor1 in dicionario1.values():
        # Percorre e compara valores do dicionário 2 com os do 1
        for valor2 in dicionario2.values():
            if valor2 == valor1:
                lista_interseccoes.append(valor2)
    return lista_interseccoes