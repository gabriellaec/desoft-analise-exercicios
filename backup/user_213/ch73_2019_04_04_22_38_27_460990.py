def remove_vogais(palavra):
    semvogais=[]
    vogais=['a','e','i','o','u']
    i=0
    while i<len(palavra):
        if palavra[i] not in vogais:
            semvogais.append(palavra[i])
        i+=1
    return semvogais
            