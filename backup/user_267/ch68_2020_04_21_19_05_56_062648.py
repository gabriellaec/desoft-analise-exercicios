def separa_trios(nomes):
    new = []
    for i in range(0, len(alunos)-1, 3):
        new[i] = nomes[i], nomes[i+1], nomes[i+2]
    return new
        