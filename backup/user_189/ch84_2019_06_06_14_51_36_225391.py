def inverte_dicionario(entrada):
    saida={}
    for key,value in entrada.items():
        if not value in saida:
            saida[value]=[key]
        else:
            saida[value].append(key)
       
        
    return saida