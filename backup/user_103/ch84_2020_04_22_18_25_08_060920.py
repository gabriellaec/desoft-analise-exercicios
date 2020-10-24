def inverte_dicionario(dicionario):
    dicio_novo={}
    for nome,idade in dicionario.items():
        if not idade in dicio_novo:
            dicio_novo[idade]=[]
        dicio_novo[idade].append(nome)
    return dicio_novo
        
        