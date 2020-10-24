def subtracao_de_listas(lista1,lista2):
    lista1= [2, 7, 3.1, 'banana']
    lista2= [2, 'banana', 'carro']
    for item in lista1:
        if item in lista2:
            lista2.remove(item)
    print(lista2)