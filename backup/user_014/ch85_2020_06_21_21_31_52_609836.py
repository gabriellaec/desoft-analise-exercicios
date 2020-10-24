with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    todas_palavras = conteudo.split()
    conta_banana = 0
    for palavra in todas_palavras:
        if palavra == 'Banana':
            palavra = 'BANANA'
        elif palavra == 'banana':
            palavra = 'BANANA'
        elif palavra == 'BaNaNa':
            palavra = 'BANANA'
    for palavra in todas_palavras:
        if palavra == 'BANANA':
            conta_banana += 1
    print(conta_banana)
            