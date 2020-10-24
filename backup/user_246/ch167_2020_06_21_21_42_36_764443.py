def bairro_mais_custoso(bairros):
    soma = {}
    nome = []
    valor = []
    for b in bairros:
        total = 0
        bairro = bairros[b]
        bairro = bairro[6:]
        for custo in bairro:
            total += custo
        valor.append(total)
        nome.append(b)
    bairro = nome[valor.index(max(valor))]
    return bairro

