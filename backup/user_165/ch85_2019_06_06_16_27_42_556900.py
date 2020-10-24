with open("macacos-me-mordam.txt","r",encoding = "utf8") as arquivo:
    conteudo = arquivo.read()
numero_banana = 0
maiusculas = conteudo.upper()
n_banana = maiusculas.count("BANANA")
print(n_banana)
