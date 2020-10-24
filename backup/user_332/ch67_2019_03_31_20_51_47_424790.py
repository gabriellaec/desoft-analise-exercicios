def alunos_impares (lista):
    grupo1 = []
    i = 0
    for a in lista:
        if i % 2!= 0:
            grupo1.append(a)
        i += 1
    return(grupo1)