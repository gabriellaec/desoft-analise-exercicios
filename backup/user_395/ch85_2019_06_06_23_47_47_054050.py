with open ("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()

novo_conteudo = conteudo.upper()
    
variavel = novo_conteudo.count("BANANA")
    
print(variavel)