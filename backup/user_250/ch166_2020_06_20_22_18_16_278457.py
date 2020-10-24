def total_do_semestre_por_bairro(dict):
    for key in dict:
        gasto = 0
        lista = dict[key][7:]
        for i in lista:
            gasto += float(i)
            
    return gasto