def total_do_semestre_por_bairro(infra):
    novo={}
    for bairros in infra:
        total=0
        gasto=6
        while gasto<=11:
            total+=infra[bairros][gasto]
            gasto+=1
        novo[bairros]=total
    return novo
        