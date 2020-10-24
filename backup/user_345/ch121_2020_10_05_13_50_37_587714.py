def subtracao_De_listas(lista1, lista2):
    resultado = lista1
    i = 0
    for i in lista1[:]:
        if i in lista2:
            result.remove(i)
    print(result)
        