def total_do_semestre_por_bairro(lista):
    total_semestre={}
    for bairro in lista.keys():
        total=0
        for i in range(7,13):
            mes = lista[bairro][:i]
            total += mes
        total_semestre[bairro]=total
        
    return total_semestre