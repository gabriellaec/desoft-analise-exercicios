with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    cont = conteudo.lower()
    esp = cont.split()
    i = 0
    for LeBron in esp:
        if LeBron == "banana":
            i += 1
    print(i)
    