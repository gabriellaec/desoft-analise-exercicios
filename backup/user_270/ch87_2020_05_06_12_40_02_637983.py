with open("churras.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
soma = 0
for i in conteudo:
    i.split(",")
    valor = i[1]*i[2]
    soma += valor
print(soma)
