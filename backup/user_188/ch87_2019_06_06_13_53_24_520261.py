with open("churras.txt", "r", encoding = "utf8") as arquivo:
    conteudo = arquivo.readlines()

lista_total = []

for valor in range(len(conteudo)):
    lista_total.append(conteudo[valor].split(","))
    
valor_total = 0

for valor in range(len(lista_total)):
    valor_total += lista_total[valor][1] * lista_total[valor][2]
    
print(valor_total)