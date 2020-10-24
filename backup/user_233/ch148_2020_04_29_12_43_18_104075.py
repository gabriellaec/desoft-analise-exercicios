def conta_letras(string):
    
    dicionario = {}
    
    for caractere in string:
        if caractere in dicionario.keys(): dicionario[caractere] += 1
        else: dicionario[caractere] = 1
    
    return dicionario