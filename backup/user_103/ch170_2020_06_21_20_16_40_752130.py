def apaga_repetidos(palavra):
    dicionario={}
    for letras in palavra:
        if letras not in dicionario:
            dicionario[letras]=1
        else:
            dicionario[letras]+=1
    return dicionario 