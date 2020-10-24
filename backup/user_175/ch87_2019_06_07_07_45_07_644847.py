with open("churras.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
    
lista_total = []

for valor in range(len(conteudo)):
    x = conteudo[valor].split(",")
    lista_total.append(x)
    
valor_total = 0

for valor in range(len(lista_total)):
    valor_total += float(lista_total[valor][1])*float(lista_total[valor][2])
    
print(valor_total)