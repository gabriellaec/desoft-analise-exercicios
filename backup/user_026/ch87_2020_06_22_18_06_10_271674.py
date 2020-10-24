with open("churras.txt","r") as arquivo:
    conteudo = arquivo.readline()
    for i in conteudo:
        preco[i] = conteudo[1]*conteudo[2]
        preco_total += preco[i]
print(preco_total)