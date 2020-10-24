def total_do_semestre_por_bairro(dicionario_bairros):
    dicionario_novo = {}
    
    for bairro in dicionario_bairros:
      dicionario_novo[bairro] = sum(dicionario_bairros[bairro][6:12])
    

    return dicionario_novo
