def total_do_semestre_por_bairro(dict):
    gasto = 0
    for key in dict:
        lista = dict[key][7:]
        for i in lista:
            gasto += float(i)
            
    return gasto