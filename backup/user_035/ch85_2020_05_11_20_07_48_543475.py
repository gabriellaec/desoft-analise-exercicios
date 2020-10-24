with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read().lower().split()
    contagem = 0
    for i in conteudo:
        if i == "banana":
            contagem += 1
    print(contagem)