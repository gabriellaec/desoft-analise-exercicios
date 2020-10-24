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
def bairro_mais_custoso(infra):
    novo=total_do_semestre_por_bairro(infra)
    mais_gasto=0
    for bairro, total in novo.items():
        if total>mais_gasto:
            mais_gasto=total
            custoso=bairro
    return custoso