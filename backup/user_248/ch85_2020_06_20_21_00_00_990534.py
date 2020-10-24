with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
    contador=0
    for p in palavras:
        if p.lower() == 'banana':
            contador+=1
    print (contador)
            