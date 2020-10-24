def total_do_semestre_por_bairro(lista):
    total_semestre={}
    for bairro in lista.keys():
        print(bairro)
        total=0
        for i in range(6,12):
            mes = lista[bairro][:i]
            print(mes)
            total = total+mes
        total_semestre[bairro] = total
        
    return total_semestre