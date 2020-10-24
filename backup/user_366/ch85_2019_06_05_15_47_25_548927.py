arquivo = open("macacos-me-mordam.txt", "r")
quantidade = 0
for linha in arquivo.readlines():
	linha.upper()

    i = 0
    while i < len(linha):
        if linha[i:i+6] == "BANANA":
            quantidade += 1
        i += 1            
    
print(quantidade)
arquivo.close()
