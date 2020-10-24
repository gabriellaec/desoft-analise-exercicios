def apaga_repetidos(string):
    ocorrencias = 0
    X = len(string)
    i = 0 
    dict = {}
    while i < X:
        if string[i] not in dict.keys():
            dict[string[i]] = 1
            i += 1
        else:
            dict[string[i]] = 1
            string.replace(string[i], '*')
            i += 1
    return string        
    