with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
    i=0
    for i in palavras:
        if len(palavras)==6:
            i+=1
    print (i)
            