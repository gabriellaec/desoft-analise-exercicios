with open ("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
    
conteudo = conteudo.casefold()
conteudo = conteudo.split()

NBananas = 0
for i in conteudo:
    if i == "banana":
       NBananas += 1