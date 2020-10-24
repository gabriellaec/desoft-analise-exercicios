with open ("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
    conteudo = conteudo.lower
    splitado=conteudo.split()
    i=0
    for x in splitado:
        if x == "banana":
            i+=1
print(i)
    