def alunos_impares(nomes):
    nomes_impares = []
    for nome in nomes:
        if int(nome[6])%2 != 0:
            nomes_impares.append(nome)
    return nomes_impares