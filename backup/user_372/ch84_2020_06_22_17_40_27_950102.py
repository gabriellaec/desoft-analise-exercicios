
def inverte_dicionario(dicionario1):
    dicionario2 = {}
    for nome in dicionario1:
        idade = dicionario1[nome]
        if idade in dicionario1:
            dicionario2[idade].append(nome)
        else: 
            dicionario2[idade] = [nome]
    return dicionario2
        
                           