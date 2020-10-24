def subtracao_de_listas(lista1, lista2):
    lista_final = []
    for item in lista1:
        if item not in lista2:
            lista_final.append(item)
    return lista_final

# lista1 = [2, 7, 3.1, 'banana', 'carro', {"palestra":"on"}, 4.33]
# lista2 = [2, 'banana', 'carro', 3.1, {"palestra":"on"}]
# lf = subtracao_de_listas(lista1,lista2)
# print(lf)