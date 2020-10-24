def total_do_semestre_por_bairro(dict):
    dict2 = {}
    for key in dict:
        gasto = 0
        lista = dict[key][7:]
        for i in lista:
            gasto += float(i)
        dict2[key] = gasto
        
    return dict2
       