def separa_trios(alunos):
    lista = []
    i = 0
    while i < len(alunos):
        a = alunos[i: i+3]
        lista.append(a)
        i += 3
    return lista