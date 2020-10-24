with open("churras.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
soma = 0
for i in conteudo:
    lis = i.split(",")
    print(lis)
    valor = int(i[1])*float(i[2])
    soma += valor
print(soma)
