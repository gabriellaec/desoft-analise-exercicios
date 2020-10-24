def conta_bigramas(palavra):
    dicionario = {}
    i=0
    bigramo= palavra[i] + palavra[i+1]
    while i<len(palavra):
        for bigramo in palavra:
            if not bigramo in dicionario:
                dicionario[bigramo] = 1
            else:
                dicionario[bigramo] += 1
        i+=1
    return dicionario