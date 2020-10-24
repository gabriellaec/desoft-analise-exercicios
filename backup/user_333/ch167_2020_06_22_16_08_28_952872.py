def total_do_semestre_por_bairro(lista):
    total_semestre={}
    for bairro in lista.keys():
        #print(lista[bairro][6:])
        seis_meses = lista[bairro][6:]
        total=0
        for i in range(len(seis_meses)):
            total += seis_meses[i]
        total_semestre[bairro] = total
        
    return total_semestre

def bairro_mais_custoso(lista):
    total_semestre = total_do_semestre_por_bairro(lista)
    print(total_semestre)
    maior_custo=''
    for bairro in total_semestre.keys():
        if maior_custo != '' and total_semestre[bairro]>total_semestre[maior_custo]:
            maior_custo=bairro
        else:
            maior_custo=bairro
    return maior_custo