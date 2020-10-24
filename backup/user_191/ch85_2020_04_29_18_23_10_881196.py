with open('macacos-me-mordam.txt','r') as arquivo:
    conteudo=arquivo.read()
    conteudo=conteudo.lower()
    print(conteudo.count())
    