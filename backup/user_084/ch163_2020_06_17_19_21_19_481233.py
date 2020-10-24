def calcula_media(alunos):
    total=0
    quantidade=0
    for c in alunos[0]:
        total+=alunos[0][c]
        quantidade+=1
    for c in alunos[1]:
        total+=alunos[1][c]
        quantidade+=1
    #for c in alunos[2]:
    #    total+=alunos[2][c]
    #    quantidade+=1
    media=total/quantidade
    return media
    
    
        