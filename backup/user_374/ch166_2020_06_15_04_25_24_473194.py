def total_do_semestre_por_bairro(dicionario_bairros):
    dicionario_novo = {}
    
    for bairro in dicionario_bairros:
        dicionario_novo[bairro] = sum(dicionario_bairros[bairro]) 
            
    return dicionario_novo
