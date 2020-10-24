def inverte_dicionario(dicionario_1):
    dicionario_novo = {}
    for nome in dicionario_1:
        for valores in dicionario_1:
            if valores not in dicionario_novo:
                dicionario_novo[valor] = []
    dicionario_novo.append(nome)
    return dicionario_novo 
            
    