with open("churras.txt","r") as arquivo:
    conteudo = arquivo.readlines()
preco = 0
for i in conteudo:
    alimentos = i.split(",")
    preco += float(alimentos[1])*float(alimentos[2])
print(preco)