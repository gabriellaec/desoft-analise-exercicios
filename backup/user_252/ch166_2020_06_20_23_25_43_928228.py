def total_do_semestre_por_bairro(infra):
    novo={}
    for e in infra:
        gasto=0
        i=0
        while i<=5:
            gasto+=infra[e][i]
            i+=1
        novo[e]=gasto
    return novo
        