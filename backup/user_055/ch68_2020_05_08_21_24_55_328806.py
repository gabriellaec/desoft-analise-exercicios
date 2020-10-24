def separa_trios(lista_alunos):
    trios = []
    i = 0
    while i < len(lista_alunos):
        trios.append(lista_alunos[i:i+2:])
        i += 1
    return trios
                     
                     
                  