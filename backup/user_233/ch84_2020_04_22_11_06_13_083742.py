def inverte_dicionario(dicionario):
    
    novo_dicionario = {}
    
    for chave in dicionario.keys():
        
        novo_dicionario[dicionario[chave]] = chave
        
    return novo_dicionario