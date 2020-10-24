with open("C:\\Users\\User\\Desktop\\p1\\Desoft\\macacos-me-mordam.txt", 'r') as arquivo:
    conteudo = arquivo.read()
    a = conteudo.upper()
    x = a.count("BANANA")
    
print(x)