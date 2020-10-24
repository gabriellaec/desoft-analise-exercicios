with open("churras.txt","r",encoding = "utf8") as arquivo:
    conteudo = arquivo.readlines()
lista = []
for valor in range(len(conteudo)):
    lista.append(conteudo[valor].split(","))
valor_churrasco = 0

for valor in range(len(lista)):
    valor_churrasco+=float(lista[valor][1])*float(lista[valor][2])
print(valor_churrasco)