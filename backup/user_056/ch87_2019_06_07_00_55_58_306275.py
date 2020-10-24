import csv
with open ("churras.txt") as arquivo:
    conteudo=csv.reader(arquivo)
    
total=0
for linha in conteudo:

    quantidade=int(linha[1])
    preco=float(linha[2])
    total+=preco*quantidade

print(total)
    
    
    