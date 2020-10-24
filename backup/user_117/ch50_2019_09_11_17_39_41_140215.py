def numero_no_indice(lista):
    yama = []
    i = 0
    while i < len(lista):
        if lista[i] == i:
            yama.append(i)
			i+=1
    return yama
            