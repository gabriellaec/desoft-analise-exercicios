def conta_letras(palavra):
    dicionario={}
    for letras in palavras:
        if not letras in dicionario:
            dicionario[letras]=1
        else:
            dicionario[letras]+=1
        return dicionario 
            
            