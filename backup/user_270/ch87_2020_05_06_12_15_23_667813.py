with open("churras.txt", "r") as arquivo:
    conteudo = arquivo.read()
conteudo.split(",")
soma = 0
for i in range(0,len(conteudo),3):
    valor = conteudo[i+1]*conteudo[i+2]
    soma += valor
print(soma)