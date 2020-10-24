with open("macacos-me-mordam.txt", "r", encoding="utf8") as file:
    conteudo = file.read()
print((conteudo.upper()).count("BANANA"))