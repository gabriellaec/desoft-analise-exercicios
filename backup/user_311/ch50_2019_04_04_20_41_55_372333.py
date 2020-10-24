def numero_no_indice(lista_num):
    conta = []
    i = 0
    while i <len(lista_num):
        if lista_num[i] == i:
            conta.append(i)
        i += 1
    return conta


    