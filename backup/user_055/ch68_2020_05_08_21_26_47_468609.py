def separa_trios(lista_alunos):
    trios = []
    i = 0
    while i < len(lista_alunos):
        trios.append(lista_alunos[i:i+3:])
        i += 3
    return trios
                     
                     
                  