with open("macacos-me-mordam", "r") as arquivo:
    conteudo = arquivo.read().lower()
    contagem = 0
    for i in conteudo:
        if conteudo[i] == "banana":
                contagem += 1
        else:
            continue
    print(contagem)