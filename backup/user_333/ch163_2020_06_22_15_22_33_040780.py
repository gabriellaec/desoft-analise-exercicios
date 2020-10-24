def calcula_media(alunos):
    soma = 0
    for i in range(len(alunos)):
        for aluno in alunos[i].key():
            soma += alunos[aluno]
        
    media = soma/len(alunos)
    return media