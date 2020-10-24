with open ('estoque.json') as arquivo:
    conteudo = arquivo.read()
    total = 0
    for d in conteudo.values():
        total += d['quantidade']*d['valor']
        return total