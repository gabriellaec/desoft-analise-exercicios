def numero_no_indice(lista):
    contador = 0
    while contador < len(lista):
        if lista[contador] == contador:
            resultado = []
            resultado.append(contador)
        contador +=1
    return resultado
        