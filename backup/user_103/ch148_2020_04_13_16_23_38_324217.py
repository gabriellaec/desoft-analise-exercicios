def conta_letras(palavra):
    dicionario={}
    for letras in palavra:
        if letras not in dicionario:
            dicionario[letras]=1
        else:
            dicionario[letras]+=1
    return dicionario 
            
            