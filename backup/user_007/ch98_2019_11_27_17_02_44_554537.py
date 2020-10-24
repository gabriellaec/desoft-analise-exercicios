def bairro_mais_custoso(dic):
    aux = total_do_semestre_por_bairro(dic)
    mais_custoso = 'bairro 0'
    max = 0
    for i in aux:
        if aux[i] >= max:
            mais_custoso = i
            max = aux[i]
    return mais_custoso