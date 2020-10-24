def aniversariantes_de_setembro(dicio_nomes_datas):
    dicio_nomdat_set = {}
    for nome, data in dicio_nomes_datas.items():
        if data[3:5] == '09':
            dicio_nomdat_set[nome] = data
    return dicio_nomdat_set
            
            
        