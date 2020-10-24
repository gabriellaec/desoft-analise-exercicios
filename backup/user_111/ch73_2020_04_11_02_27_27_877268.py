def remove_vogais(palavra):
    i=0
    vogais=['a','e','i','o','u']
    palavra2=[]
    while i<len(palavra):
        if palavra[i] not in vogais:
            palavra2.append(palavra[i])
        i+=1
    return palavra2