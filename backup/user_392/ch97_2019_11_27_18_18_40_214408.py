def total_do_semestre_por_bairro(x):
    lista = []
    for e,v in x.items():
        novo = sum(v[6:])
        lista.append(novo)
    return lista