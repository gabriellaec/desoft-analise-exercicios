def encontra_maximo(lista):
    max_i = 0
    i = 0 
    while i<len(lista):
        j = 0
        linha = lista[i]
        while j<len(linha):
            if linha[j]>max_i:
                max_i = linha[j]
                j+=1
            else:
                j+=1
        i+=1
    return max_i