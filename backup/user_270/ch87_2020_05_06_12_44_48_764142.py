with open("churras.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
soma = 0
for i in conteudo:
    lis = i.strip().split(",")
    valor = int(lis[1])*float(lis[2])
    soma += valor
print(soma)
