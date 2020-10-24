conta_palavras = 0
with open('texto.txt','r') as f:
    linha = f.readline()
    while linha:
        x = linha.split()
        for palavra_linha in x:
            conta_palavras += 1
print(conta_palavras)
         