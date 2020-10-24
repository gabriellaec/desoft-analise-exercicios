def total_do_semestre_por_bairro(gasto):
    novod = {}
    for k,v in gasto.items():
        novod[k]= v[6]+ v[7]+ v[8] + v[9] + v[10] + v[11]
    return novod