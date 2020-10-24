with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    todas_palavras = conteudo.split()
    conta_banana = 0
    for palavra in todas_palavras:
        if palavra == 'Banana':
            palavra = 'banana'
        elif palavra == 'BANANA':
            palavra == 'banana'
        elif palavra == 'BaNaNa':
            palavra == 'banana'
        if palavra == 'banana':
            conta_banana += 1
    print(conta_banana)
            