def lista_sufixos(palavra):
    lista = []
    for i in range(0, len(palavra)):
        lista.append(palavra[i:])
    print(lista)
    return lista

        