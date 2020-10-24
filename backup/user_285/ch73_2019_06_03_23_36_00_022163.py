def remove_vogais(palavra):
    semvogais=[]
    i=0
    tamanho=len(palavra)
    while i<len(palavra):
        if palavra[i]!="a":
            semvogais.append(palavra[i])
        if palavra[i]!="e":
            semvogais.append(palavra[i])
        if palavra[i]!="i":
            semvogais.append(palavra[i])
        if palavra[i]!="o":
            semvogais.append(palavra[i])
        if palavra[i]!="u":
            semvogais.append(palavra[i])
        i+=1
    return semvogais


    