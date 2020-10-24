def calcula_media(alunos):
    soma = 0
    n=0
    for i in range(len(alunos)):
        for aluno in alunos[i].keys():
            soma += alunos[i][aluno]
            n+=1
        
    media = soma/n
    return media