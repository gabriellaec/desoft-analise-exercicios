def frase(nome):
    with open(nome, "r") as arquivo:
        conteudo = arquivo.read()
        contagem = 0
        for i in conteudo:
            if conteudo[i] == "Banana" or "BANANA" or "banana":
                contagem += 1
            else:
                continue
    return contagem
print(frase("macacos-me-mordam.txt"))