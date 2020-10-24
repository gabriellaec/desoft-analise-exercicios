import csv
total=0
with open ("churras.txt") as arquivo:
    conteudo=csv.reader(arquivo)
	for linha in conteudo:
    	quant=float(linha[1])
    	preco=float(linha[2])
    	total+=quant*preco

print(total)
    
    
    