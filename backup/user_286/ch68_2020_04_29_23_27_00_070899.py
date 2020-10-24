def separa_trios(lista_alunos):
    lista_final = []
    i = 0
    for a in range(int(len(lista_alunos)/3)):
        lista = []
        p = 0
        while p < 3:
            lista.append(lista_alunos[i])
            p += 1
            i += 1
        lista_final.append(lista)

    lista_sobra = []
    if len(lista_alunos) % 3 != 0:
        if len(lista_alunos) % 3 == 1:
            lista_sobra.append(lista_alunos[-1])
        elif len(lista_alunos) % 3 == 2:
            lista_sobra.append(lista_alunos[-2])
            lista_sobra.append(lista_alunos[-1])
    lista_final.append(lista_sobra)
    
    return lista_final  