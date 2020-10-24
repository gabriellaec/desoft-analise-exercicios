def total_do_semestre_por_bairro(empresa):
    novo = {}
    for bairro in empresa:
        novo[bairro]= 0
        for mes in empresa[bairro][6:]:
            novo[bairro] += mes
    return novo
def bairro_mais_custoso(lista):
    valor= []
    nome= []
    nome.append(0)
    valor.append(0)
    meses= total_do_semestre_por_bairro(lista)
    for i in meses:
        if meses[i] > valor[0]:
            valor[0] = meses[i]
            nome[0] = i
    return nome[0]