def junta_nomes(nomes_homem, nomes_mulher, sobrenomes):
    nomes_completos = []
    for nome_homem in nomes_homem:
        for sobrenome in sobrenomes:
            nomes_completos.append(nome_homem + ' ' + sobrenome)
        for sobrenome in sobrenomes:
            nomes_completos.append(nome_mulher + ' ' + sobrenome)
    return nomes_completos