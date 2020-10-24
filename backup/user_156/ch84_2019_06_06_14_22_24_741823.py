def inverte_dicionario(dicionario):
    dicionarionew = {}
    
    for nome,idade in dicionario.items():
        if idade in dicionarionew:
            dicionarionew[idade].append(nome)
        else:
            dicionarionew[idade] = [nome]
    return dicionarionew
        
        
        
    