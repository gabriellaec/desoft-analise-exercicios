def total_do_semestre_por_bairro(infra):
    novo={}
    for bairros in infra:
        total=0
        mes=6
        while mes<=11:
            total+=infra[bairros][mes]
            mes+=1
        novo[bairros]=total
    return novo
        