def conta_bigramas (string):
    dicionario = {}
    i = 0
    while i < len(string)-1:
        bigrama = string[i:i+2]
        if string[i] not in dicionario:
            string[i] = 1
        else:
            string[i] += 1
    return string
        
        