with open('churras.txt', 'r') as arquivo:
    conteudo = arquivo.readline()
    conteudo_split = []
    custo_total = 0
    i = 0
    for k in range(0, len(conteudo)):
        conteudo_split.append(conteudo[k].split)
        custo = conteudo_split[i+1] * conteudo_split[i+2]
        custo_total += custo
        i+=3
print(custo_total)
    