def inverte_dicionario(d1):
    d2={}
    for nome_e_idade in d1.items():
        nome=nome_e_idade[0]
        idade=nome_e_idade[1]
        if idade in d2.keys():
            d2[idade].append(nome)
        else:
            d2[idade]=[nome]
    return d2
        
    