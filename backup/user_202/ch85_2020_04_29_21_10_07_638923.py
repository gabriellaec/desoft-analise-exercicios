with open ('macacos-me-mordam.txt', 'r') as arquivo:
    texto = arquivo.read()
    normal = texto.lower()
    palavras = normal.split()
    c = 0
    for palavra in palavras:
        if palavra == 'banana':
            c += 1
    print(c)