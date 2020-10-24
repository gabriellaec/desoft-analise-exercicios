with open('macacos-me-mordam.txt', 'r') as arq:
    texto=arq.read()
    conteudo=texto.lower()
    print(conteudo.count('banana'))
    
    