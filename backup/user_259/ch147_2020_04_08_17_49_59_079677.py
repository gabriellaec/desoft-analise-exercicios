def mais_frequente(lista):
    ocorrencias = {}
    for i in lista:
        ocorrencias[i] = 0
    for i in lista:
        if i in ocorrencias:
            ocorrencias[i]+=1
    contadores = ocorrencias.values()
    max = 0
    for i in contadores:
        if len(lista)==1:
            max = lista[0]
            return max
        for j in contadores:
            if i>j:
                max = i
    for i in ocorrencias:
        if ocorrencias[i] == max:
            return i