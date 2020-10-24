def total_do_semestre_por_bairro(bairros):
    dados = {}
    for key in bairros:
        i = 0
        while i < 6:    
            bairros[key].pop(i)
            i += 1
        dados.update({key:sum(bairros[key])})
    return dados
