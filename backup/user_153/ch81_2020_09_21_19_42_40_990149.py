def interseccao_valores(dicionario1, dicionario2):
    lista_interseccao = []
    for value in dicionario1.values():
        if value in dicionario2.values():
            lista_interseccao.append(value) 

    return lista_interseccao

# d1 = { "banana": 1, "papagaio": 2, "bola": 3}
# d2 = { "bola": 5, "banana": 2, "pneu": 7}
# print(interseccao_valores(d1,d2))