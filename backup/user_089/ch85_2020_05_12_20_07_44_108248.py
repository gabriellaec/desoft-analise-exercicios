with open("macacos-me-mordam.txt","r") as arquivo:
    conteudo = arquivo.read()
    x = conteudo.split()
    soma = 0
    for e in x:
        if e.lower() == "banana":
            soma += 1
print(soma)