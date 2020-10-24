def junta_nome_sobrenome(nomes, sobrenomes):
    nomes_completos = []
    tamanho = len(nomes)
    x = 0
    while x < tamanho:
        nomes_completos.append('{} {}'.format(nomes[x], sobrenomes[x]))
        x += 1
    return nomes_completos
        