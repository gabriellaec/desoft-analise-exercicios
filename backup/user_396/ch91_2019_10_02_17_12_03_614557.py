with open("palavras.txt", "r") as arquivo:
    conteudo = arquivo.read()
    soma = 0
    for e in conteudo:
        if 'a' == e or 'A' == e:
            soma +=1
    print(soma)