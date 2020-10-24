def estritamente_crescente(lista):
    contador=1
    lista_2=[lista[0]]
    while contador < len(lista):
        if lista[contador]> lista_2[contador-1]:
            lista_2.append(lista[contador])
        contador +=1
    return lista_2