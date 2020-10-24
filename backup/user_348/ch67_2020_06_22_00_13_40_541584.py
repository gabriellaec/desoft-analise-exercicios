def alunos_impares (nomes):
    #determina uma lista apenas com os elementos da lista inicial ímpares (começa do 1 e vai até o final pulando de 2 em 2)
    alunos = nomes[1::2]
    return alunos

print(alunos_impares (['Aluno 0', 'Aluno 1']))
       