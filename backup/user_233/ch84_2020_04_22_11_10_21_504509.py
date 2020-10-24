def inverte_dicionario(dicionario):
    
    novo_dicionario = {}
    
    for chave in dicionario.keys():

        if dicionario[chave] in novo_dicionario.keys():
            novo_dicionario[chave].append(chave)
        
        else:
            novo_dicionario[dicionario[chave]] = [chave]
        
    return novo_dicionario