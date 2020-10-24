def conta_bigramas (string):
    dicionario = dict()
    for i in range (0,len(string)-1):
        par_de_letras = string[i]+string[i+1]
        if par_de_letras not in dicionario:
            dicionario [par_de_letras] = 1 
        else:
            dicionario [par_de_letras]+= 1
        print (dicionario)
        return dicionario