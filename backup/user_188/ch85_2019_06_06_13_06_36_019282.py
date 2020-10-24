with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.readlines()

numero_de_bananas = 0
    
for valor in range(len(conteudo)):
    if conteudo[valor].upper() == "BANANA":
        numero_de_bananas += 1
        
print(numero_de_bananas)