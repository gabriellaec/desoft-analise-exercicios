def alunos_impares(l1):
    lista = list()
    for i in l1:
        if len(i) % 2 != 0:
            lista.append(i)    
    return lista