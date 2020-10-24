with open ("macacos-me-mordam.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    soma = 0
    for i in x:
        soma += 1
    print (soma)