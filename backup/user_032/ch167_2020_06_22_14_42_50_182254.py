def bairro_mais_custoso(dicionario):
    dic = {}
    nome = ' '
    val = 0
    for bairro,valores in dicionario.items():
        v = valores[6:]
        total = 0
        for x in v:
            total += x
        dic[bairro] = total
        if total > val:
            val = total
            nome = bairro
    return nome