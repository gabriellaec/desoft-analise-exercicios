def junta_nomes(nomeM, nomeF, sobrenome):
    lista_nomes = []
    for i in sobrenome:
        for j in nomeM: lista_nomes.append(j+" "+i)
        for j in nomeF: lista_nomes.append(j+" "+i)
    return lista_nomes