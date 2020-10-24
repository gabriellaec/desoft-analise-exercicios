with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
novo_conteudo = arquivo.upper()
n = novo_conteudo.count("BANANA")
print(n)