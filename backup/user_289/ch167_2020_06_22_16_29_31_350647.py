def bairro_mais_custoso(dicionario)
    def total_do_semestre_por_bairro(dicionario):
        dict = {}
        for bairro, value in dicionario.items():
            semester = 0 
            for mes in range (6, 12):
                semester += value[mes]
            dict[bairro] = semester
        return dict

    call = total_do_semestre(dicionario)
    for bairro, gasto_semestral in call.items:
        