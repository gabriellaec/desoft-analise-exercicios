def interseccao_chaves(dicionario1, dicionario2):
    lista_interseccao = []
    for key in dicionario1.keys():
        if key in dicionario2.keys():
            lista_interseccao.append(key) 

    return lista_interseccao

# d1 = { "banana": 1, "papagaio": 2, "bola": 3}
# d2 = { "bola": 5, "banana": 2, "pneu": 7}
# print(interseccao_chaves(d1,d2))