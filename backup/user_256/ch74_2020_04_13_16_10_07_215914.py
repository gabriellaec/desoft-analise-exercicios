def conta_bigramas(palavra):
    dicionario = {}
    i=0
    while i<len(palavra):
        bigramo= palavra[i] + palavra[i+1]
            if not bigramo in dicionario:
                dicionario[bigramo] = 1
            else:
                dicionario[bigramo] += 1
            i+=1
    return dicionario