with open ("macacos-me-mordam.txt", "r") as arquivo:
    ler = arquivo.read()
    a = ler.split()
    lista = []
    if i in a:
        if i.lower() == "banana":
            lista.append(i)
    print(len(lista))
        