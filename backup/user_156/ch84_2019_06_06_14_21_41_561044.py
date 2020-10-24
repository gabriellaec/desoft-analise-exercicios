def inverte_dicionario(dicionario):
    dicionario = {'Ana': 19, 'Bruno': 18, 'Joao': 19}
    dicionarionew = {}
    
    for nome,idade in dicionario.items():
        if idade in dicionarionew:
            dicionarionew[idade].append(nome)
        else:
            dicionarionew[v] = [k]
    return dicionarionew
        
        
        
    