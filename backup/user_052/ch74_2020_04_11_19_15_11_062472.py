def conta_bigramas (string):
    dicionario = {}
    i = 0
    while i < len(string)-1:
        bigrama = string[i:i+2]
        if string[i+2] not in bigrama:
            string[i] = 1
        else:
            string[i] += 1
    return string
        
        