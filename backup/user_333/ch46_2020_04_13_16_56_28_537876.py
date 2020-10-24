def numero_no_indice(lista):
    resultado=[]
    for i in range(len(lista)):
        if i==lista[i]:
            resultado.append(lista[i])
    return resultado
