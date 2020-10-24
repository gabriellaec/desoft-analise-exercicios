with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readlines() #Retorna lista de strings de cada linha
conteudo.split(',')
print(conteudo)
custo_total = 0
