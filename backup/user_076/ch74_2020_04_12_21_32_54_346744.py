def conta_bigramas (string):
    dicionario = dict()
    par_de_letras = string[i]+string[i+1]
    for par_de_letras in string:
        if par_de_letras not in dicionario:
            dicionario [i] = 1 
        else:
            dicionario [i]+= 1
        return dicionario