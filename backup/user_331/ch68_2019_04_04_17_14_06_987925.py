def separa_trios(lista_alunos):
    i=0
    lista_trios=[]
    while i<len(lista_alunos):
        lista_trios.append(lista_alunos[i:i+3])
        i+=3
    return lista_trios
    