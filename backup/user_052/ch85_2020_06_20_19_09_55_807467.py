with open ("macacos-me-mordam.txt", "r") as arquivo:
    ler = arquivo.read()
    x = ler.split()
    soma = 0
    if x not in ler:
        soma += 1
    print (soma)