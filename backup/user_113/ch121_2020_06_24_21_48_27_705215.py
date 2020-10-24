def subtracao_de_listas(lista1,lista2):
    for item in lista1:
        if item in lista2:
            lista1.remove(item)
    if lista1==[] or lista2==[]:
        False
    print(lista1)