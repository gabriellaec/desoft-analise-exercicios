with open("macacos-me-mordam.txt", "r", encoding = "utf8") as arquivo:
    conteudo = arquivo.read()

numero_de_bananas = 0

CONTEUDO = conteudo.upper()
    
if CONTEUDO.find("BANANA"):
    numero_de_bananas += 1
        
print(numero_de_bananas)