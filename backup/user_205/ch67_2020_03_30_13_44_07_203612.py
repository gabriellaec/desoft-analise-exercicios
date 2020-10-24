def alunos_impares(lista):
    opa=[]
    for aluno in lista:
        if aluno%2!=0:
            opa.append(aluno)
    return opa