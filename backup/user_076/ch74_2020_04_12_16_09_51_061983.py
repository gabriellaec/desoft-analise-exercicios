def conta_bigramas (string):
    dicionario = dict()
    for string[i]+string[i+1] in string:
        if i not in dicionario:
            dicionario [i] = 1 
        else:
            dicionario [i]+= 1
        return dicionario