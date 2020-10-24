with open ("macacos-me-mordam.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    soma = 0
    for a in x:
        w = x[a].lower
        for i in w:
            soma += 1
    print (soma)
