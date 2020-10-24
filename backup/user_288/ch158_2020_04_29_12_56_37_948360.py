conta_palavras = 0
with open(nome, 'r') as arquivo:
    conteudo = arquivo.readline()
    while conteudo:
        x = conteudo.split()
        for palavras in x:
            conteudo = arquivo.readline()
            conta_palavras += 1
print (conta_palavras)

