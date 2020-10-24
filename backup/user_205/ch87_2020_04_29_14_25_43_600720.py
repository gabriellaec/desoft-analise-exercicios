with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines() #Retorna lista de strings de cada linha
conta_final = 0
for i in range(len(conteudo)):
    separado = conteudo[i].split(",")
    custo_total = float(separado[1]) * float(separado[2]) 
    conta_final += custo_total
print (conta_final)
