def total_do_semestre_por_bairro(dicionario):
    dicionario2={}
    for bairro in dicionario:
        for valor in range (6,11):
            if not bairro in dicionario2:
                dicionario2[bairro] = dicionario[bairro][valor]
            else:
                dicionario2[bairro] += dicionario[bairro][valor]
                
    return dicionario2
  