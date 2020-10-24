with open ("macacos-me-mordam.txt","r") as arquivo:
    texto = arquivo.read()
    print(texto.lower().count("banana"))
          