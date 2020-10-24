with open("macacos-me-mordam.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.upper()
    x = a.count("BANANA")
    
print(x)