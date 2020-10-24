def calcula_media(lista):
    soma = 0
    num = 0
    for dic in lista:
        for key, value in dic.items():
            soma += value
            num += 1
    return soma/num

# alunos = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5}, {"aluno4": 6} ]
# med = calcula_media(alunos)
# print(med)