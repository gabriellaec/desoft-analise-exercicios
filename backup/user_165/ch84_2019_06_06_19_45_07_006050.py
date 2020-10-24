def inverte_dicionario(dicionario_1):
    dicionario_novo = {}
    for nome,valores in dicionario_1.items():
        if valores not in dicionario_novo:
            dicionario[nome] = [valores]
        else:
            dicionario[nome].append[valores]
    return dicionario_novo 
            
    