def aniversariantes_de_setembro (nomes_nascimento):
    setembro = dict()
    for i in nomes_nascimento:
        if i[5]==9:
            setembro[i] = nomes_nascimento[i]
    return setembro