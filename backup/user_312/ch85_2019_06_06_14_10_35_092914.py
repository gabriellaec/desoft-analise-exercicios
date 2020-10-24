with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo = conteudo.lower()
loop = True
i=0
while loop:
    try:
        posicao = conteudo.find("banana")
    except:
        loop = False
    i+=1
    conteudo.replace("banana", "oi", 1)
print(i)