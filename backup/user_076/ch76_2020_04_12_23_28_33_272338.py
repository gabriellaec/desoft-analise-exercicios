def aniversariantes_de_setembro (nomes_nascimento):
    nomes_nascimento = dict()
    setembro = dict()
    for i in nomes_nascimento:
        if i[5]==7:
            setembro[i] = nomes_nascimento[i]
    return setembro