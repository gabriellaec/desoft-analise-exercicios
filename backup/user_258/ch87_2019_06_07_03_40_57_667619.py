with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readline()
    for k in range(0,len(conteudo)):
        conteudo[k] = conteudo[k].split(",")
custo_total = 0
for v in range(1, len(conteudo), 3):
    custo = conteudo [v] * conteudo [v+1]
    custo_total += custo
print(custo_total)
    
    