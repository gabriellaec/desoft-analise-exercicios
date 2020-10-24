with open ("macacos-me-mordam.txt" , "r") as arquivo:
    conteudo = arquivo.read()
    
numero_de_bananas = 0

maiusulas = conteudo.upper()

numero_de_bananas = maiusculas.count("BANANA")

print (numero_de_bananas)