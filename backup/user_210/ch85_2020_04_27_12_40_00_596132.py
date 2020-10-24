with open('macacos-me-mordam.txt', 'r') as file:
    conteudo = file.read().upper()
    print(conteudo.count("BANANAS"))
    