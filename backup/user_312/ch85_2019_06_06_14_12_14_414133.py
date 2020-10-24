with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.lower()
loop = True
i=0
while conteudo.find("banana"):
    conteudo.replace("banana", "oi", 1)
    i+=1
print(i)