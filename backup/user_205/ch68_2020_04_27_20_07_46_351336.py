def separa_trios(alunos):
    lista = []
    i = 0 
    while i<len(alunos):
        trio = alunos[i:i+3]
        lista.append(trio)
        i+=3
    return lista
        
        
        