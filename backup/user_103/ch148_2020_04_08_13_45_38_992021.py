def conta_letras(letras):
    dicionario={}
    for i in letras:
        if not letras in dicionario:
            dicionario[letras]=1
        else:
            dicionario[letras]+=1
        return dicionario 
            
            