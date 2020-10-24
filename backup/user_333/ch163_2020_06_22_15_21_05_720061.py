def calcula_media(alunos):
    soma = 0
    for aluno in alunos.key():
        soma += alunos[aluno]
        
    media = soma/len(alunos.key())
    return media