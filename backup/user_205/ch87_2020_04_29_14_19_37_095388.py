with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines() #Retorna lista de strings de cada linha
print(conteudo)
custo_total = 0
for i in range(len(conteudo)):
    
    print (conteudo[i].split(","))
