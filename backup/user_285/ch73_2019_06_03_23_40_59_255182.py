def remove_vogais(palavra):
    semvogais=[]
    i=0
    tamanho=len(palavra)
    while i<len(palavra):
        if palavra[i]!="a" and palavra[i]!="e" and palavra[i]!="i" and palavra[i]!="o" and palavra[i]!="u" :
            semvogais.append(palavra[i])
        i+=1
    return semvogais




    