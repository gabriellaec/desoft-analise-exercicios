def total_do_semestre_por_bairro(dicionario):
    dict = {}
    for bairro, value in dicionario.items():
        semester = 0 
        for mes in range (6, 12):
            semester += value[mes]
        dict[bairro] = semester
    return dict