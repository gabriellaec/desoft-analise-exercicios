def interseccao_valores(dicionario1,dicionario2):
    lista = []
    for valor1 in dicionario1.values():
        for valor2 in dicionario2.values():
            if valor1 == valor2:
                lista.append(valor1)
    return lista