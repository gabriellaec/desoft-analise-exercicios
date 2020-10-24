with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista=conteudo.split()
    a=lista.count('banana')
    print(a)