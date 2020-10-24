def calcula_media(alunos):
    media = 0
    for aluno in alunos:
        contador = 0 
        for nota in alunos[aluno]:
            contador += alunos[aluno][nota]
            if contador %3 == 6:
                media = contador
    return media
                

    
    
alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ]

print(calcula_media(alunos))