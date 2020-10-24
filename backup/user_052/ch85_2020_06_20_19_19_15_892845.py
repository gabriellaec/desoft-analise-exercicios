with open ("macacos-me-mordam.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    soma = 0
    for a in x:
        if a.lower() == "banana":
            soma += 1
    print (soma)

