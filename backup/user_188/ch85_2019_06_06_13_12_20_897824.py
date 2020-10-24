with open("macacos-me-mordam.txt", "r", encoding = "utf8") as arquivo:
    conteudo = arquivo.read()

numero_de_bananas = 0

for valor in range(len(conteudo)):
    conteudo[valor].upper()
    
for "BANANA" in conteudo:
    numero_de_bananas += 1
        
print(numero_de_bananas)