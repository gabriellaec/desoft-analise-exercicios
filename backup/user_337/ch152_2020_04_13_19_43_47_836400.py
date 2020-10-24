def verifica_preco(titulo, nomes_cores, cores_precos):
    for i in nomes_cores:
        if i == titulo:
            cor = nomes_cores[i]
    for a in cores_precos:
        if a == cor:
            preco = cores_precos[a]
    return preco