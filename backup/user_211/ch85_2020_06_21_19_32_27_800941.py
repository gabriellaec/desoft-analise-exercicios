with open(macacos-me-mordam.txt) as arquivo:
    conteudo=arquivo.read()
    palavras=conteudo.split()
    minusculas=[]
    for i in palavras:
        minusculas.append(i.lower())
    print(minusculas.count('banana')+1)