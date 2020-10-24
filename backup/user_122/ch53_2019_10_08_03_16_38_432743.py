def inverte_lista(lista):
    lista_original = input("Qual a lista?")
    lista_invertida = []
        for num in lista_original[-1::-1]:
            lista_invertida.append(num)
    return lista_invertida