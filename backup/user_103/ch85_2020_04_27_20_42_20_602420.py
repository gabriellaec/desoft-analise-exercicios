with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista=conteudo.split()
    b=lista.lower()
    a=b.count('banana')
    print(a)