with open ('estoque.json') as arquivo:
    conteudo = arquivo.read()
    total = 0
    for v in conteudo.values():
        total += v['quantidade']*v['valor']
    print(total)