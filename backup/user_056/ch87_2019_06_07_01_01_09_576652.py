import csv
total=0
with open ("churras.txt") as arquivo:
    consumo=csv.reader(arquivo)
	for linha in consumo:
    	quantidade=int(linha[1])
    	preco=float(linha[2])
    	total+=quantidade*preco

print(total)
    
    
    