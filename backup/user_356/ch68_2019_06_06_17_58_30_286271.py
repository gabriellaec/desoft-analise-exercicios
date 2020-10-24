def separa_trios(lista_alunos):
    lista_trios=[]
    i=0
    while i<len(lista_alunos):
        lista_trios.append(lista_alunos[i:i+3])
        i+=1
    return lista_trios