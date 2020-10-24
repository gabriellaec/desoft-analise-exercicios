with open("macacos-me-mordam.txt","r") as arquivo:
    conteudo = arquivo.read()
    soma = 0
    for e in conteudo:
        if e.lower() == "banana":
            soma += 1
print(soma)