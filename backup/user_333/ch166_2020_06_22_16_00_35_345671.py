def total_do_semestre_por_bairro(lista):
    total_semestre={}
    for bairro in lista.keys():
        seis_meses = lista[bairro][:6]
        total=0
        for i in range(seis_meses):
            total += seis_meses[i]
        total_semestre[bairro] = total
        
    return total_semestre