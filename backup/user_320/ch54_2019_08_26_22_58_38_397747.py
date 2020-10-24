def junta_sobrenome(nome, sobrenome):
    nomeCompleto = zip(nome, sobrenome)
    nomes = []
    for elemento in list(nomeCompleto):
        nomes.append(' '.join(elemento))
    return nomes