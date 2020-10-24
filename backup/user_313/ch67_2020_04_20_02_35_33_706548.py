def alunos_impares(l1):
    lista = list()
    if len(l1) == 1:
        pass
    else:
        for i in range(0,len(l1)):
            if i % 2 != 0:
                lista.append(l1[i])
                
    return lista