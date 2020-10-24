def interseccao_valores(dicionario1,dicionario2):
    lista = []
    for chave1,valor1 in dicionario1.values():
        for chave2,valor2 in dicionario2.values():
            if valor1 == valor2:
                lista.append(valor1)
    return lista