def invert_dicionario(x):
	dici={}
    for nome, idade in x.items():
        if idade not in dici:
            dici[idade]=[nome]
        else:
            dici[idade].append(nome)
            
        return dici
            
    