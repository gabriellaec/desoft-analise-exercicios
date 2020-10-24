def mais_frequente (lista):
    dicionario = {}
    for i in lista:
        if i not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    vmax = 0
    for k,v in dicionario.items():
        if v>vmax:
            v = vmax
            pergunta = k
    return pergunta
    
        
        