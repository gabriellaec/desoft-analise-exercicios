def separa_trios(alunos):
    
    trios = []
    trio = 0
    
    for i in range(len(alunos)):
        
        if i % 3 == 0:
            trio += 1
            trios.append([])
        
        trios[trio].append(alunos[i])
    
    return trios