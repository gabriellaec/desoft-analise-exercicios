def numero_no_indice(lista):
    cont = 0
    num_iguais_aos_indices = []
    while len(lista)>cont:
        if lista.index(lista[cont]) == lista[cont]:
            num_iguais_aos_indices.append(lista[cont])
            cont+=1
            return num_iguais_aos_indices
        else:
            num_iguais_aos_indices =[]
            return num_iguais_aos_indices