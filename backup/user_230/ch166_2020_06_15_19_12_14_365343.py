def total_do_semestre_por_bairro (dicio):
    gasto=0
    novo_dict={}
    for bairro in dicio:
        novo_dict[bairro]=sum(dicio[bairro][6:])
    return novo_dict