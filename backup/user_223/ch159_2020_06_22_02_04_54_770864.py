with open ('estoque.json') as arquivo:
    conteudo = arquivo.read()
    for d in conteudo.values():
        for v in d.values():
            if v == float:
                