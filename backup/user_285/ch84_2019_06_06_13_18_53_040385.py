def inverte_dicionario(idades):
    dicn={}
    for nome,idade in idades.items():
        if idade not in dicn:
            dicn[idade]=[nome]
        else:
            listeras=dicn[idade]
        	dicn[idade]=listeras.append([nome])
    return dicn