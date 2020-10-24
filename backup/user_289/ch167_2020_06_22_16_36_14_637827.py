def total_do_semestre_por_bairro(dicionario):
    dict = {}
    for bairro, value in dicionario.items():
        semester = 0 
        for mes in range (6, 12):
            semester += value[mes]
        dict[bairro] = semester
    return dict
def bairro_mais_custoso(dicionario):
    call = total_do_semestre_por_bairro(dicionario)
    maior_gasto = 0
    for bairro, gasto_semestral in call.items:
        if gasto_semestral > maior_gasto:
            maior_gasto = gasto_semestral
            nome_bairro = bairro
    return nome_bairro
        