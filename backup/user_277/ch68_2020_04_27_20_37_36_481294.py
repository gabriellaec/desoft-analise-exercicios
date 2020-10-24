def separa_trios(lista):
    trio=[]
    i=0
    while i<len(lista):
        alunos=lista[i:i+3]
        trio.append(alunos)
        i+=3
    return trio
        