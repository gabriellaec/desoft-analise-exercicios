with open ("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
    string = conteudo.lower()
    sub_string = "banana"
    contador = string.count(substring)
    print(contador)
    