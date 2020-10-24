with open("macacos-me-mordam.txt","r",encoding = "utf8") as arquivo:
    conteudo = arquivo.read()
    
    
num_bananas = 0

maiusculas = conteudo.upper()

num_bananas = maiusculas.count("BANANA")

print(num_bananas)
