def total_do_semestre_por_bairro(dicionario_bairros):
    dicionario_novo = {}
    
    for bairro in dicionario_bairros:
      dicionario_novo[bairro] = sum(dicionario_bairros[bairro][6:12])
    

    return dicionario_novo

def bairro_mais_custoso(dicionario_bairros):
    dicionario_calculado =  total_do_semestre_por_bairro(dicionario_bairros)

    var_contagem = 0
    var_nome = 'inicio'

    for bairro in dicionario_calculado:
        if dicionario_calculado[bairro] >= var_contagem:
            var_contagem = dicionario_calculado[bairro]
            var_nome = bairro
    
    return var_nome
