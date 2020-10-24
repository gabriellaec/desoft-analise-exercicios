def conta_bigramas(palavra):
    dicionario={}
    soma=0
    for par1 and par2 in palavra:
        if not par1 and par2 in dicionario:
            dicionario[par1] and dicionario[par2]=soma
            soma=1
        else:
            dicionario[par1] and dicionario[par2]=soma
            soma+=1
        print (dicionario)