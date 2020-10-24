import csv
with open ("churras.txt") as arquivo:
    conteudo=csv.reader(arquivo)
    
total=0
for linha in conteudo:

    quantidade=float(conteudo[1])
    preco=float(conteudo[2])
    total+=preco*quantidade

print(total)
    
    
    