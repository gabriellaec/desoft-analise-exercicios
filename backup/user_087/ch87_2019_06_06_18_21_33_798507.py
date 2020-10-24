import csv
custo = 0
with open('churras.txt', 'r') as arquivo:
    conteudo = csv.reader(arquivo)
    for linha in conteudo:
    	quantidade = float(linha[1])
    	valor = float(linha[2])
    	custo += quantidade*valor


print(custo)
        