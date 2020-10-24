def numero_indice(lista):
    lista_vazia=[]
    cont = 0
    while cont < len(lista):
        if lista[cont] == cont:
            lista_vazia.append(lista[cont])
        cont += 1
    return lista_vazia