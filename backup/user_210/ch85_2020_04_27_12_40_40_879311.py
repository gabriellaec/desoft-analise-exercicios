with open('macacos-me-mordam.txt', 'r') as file:
    conteudo = str(file.read()).upper()
    print(conteudo.count("BANANA"))
    