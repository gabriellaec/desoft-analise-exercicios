with open("churras.txt","r",encoding = "utf8") as arquivo:
    conteudo = arquivo.readlines()
lista = []
for valor in range(len(conteudo)):
    lista.append(conteudo[valor].split(","))
    
i = 0
valor_churrasco = 0
while i <=len(dict):
    valor_churrasco = dict[i]*dict[i+1]
    i+=1
print(valor_churrasco)
