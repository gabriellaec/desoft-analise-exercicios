with open("macacos-me-mordam.txt", "r", encoding = "utf8") as arquivo:
    conteudo = arquivo.read()
    
maiusculas = conteudo.upper()

numero_de_bananas = maiusculas.count("BANANA")

print(numero_de_bananas)