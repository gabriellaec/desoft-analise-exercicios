with open ('estoque.json') as arquivo:
    conteudo = arquivo.read()
    total = 0
    for d in conteudo.values():
        for v in d.values():
            total += v['quantidade']*v['valor']
    print(total)