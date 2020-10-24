def total_do_semestre_por_bairro(lista):
    total_semestre={}
    for bairro in lista.keys():
        6meses = lista[bairro][:6]
        total=0
        for i in range(6meses):
            total += 6meses[i]
        total_semestre[bairro] = total
        
    return total_semestre