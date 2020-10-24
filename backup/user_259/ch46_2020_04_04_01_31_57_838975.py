def numero_no_indice(lista):
    indice = [i for i in range(len(lista))]
    iguais = []
    i = 0 
    while i<len(lista):
        if i == lista[i]:
            iguais.append(lista[i])
            i+=1
        else:
            i+=1
    return iguais
        