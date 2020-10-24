def total_do_semestre_por_bairro(dict):
    novodict = {}
    i = 0
    soma = 0
    while i <= len(dict):
        soma = soma + dict[i][5]+dict[i][6]+dict[i][7]+dict[i][8]+dict[i][9]+dict[i][10]+dict[i][11]
        novodict['total gasto do bairro'] = soma 
        i += 1
    print(novodict)
        