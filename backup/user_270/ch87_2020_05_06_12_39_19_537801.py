with open("churras.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
conteudo.split(",")
soma = 0
for i in conteudo:
    valor = i[1]*i[2]
    soma += valor
print(soma)
