def separa_trios(alunos):
    lista = []
    i = 0
    while i<len(alunos):
        lista.append(list(alunos[i:3+i]))
        i += 3
    return lista
