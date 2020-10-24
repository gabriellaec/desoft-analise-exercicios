import csv
with open ("churras.txt") as arquivo:
    conteudo=csv.reader(arquivo)
    
total=0
for linha in conteudo:
    lista=linha.split(",")
    quantidade=int(lista[1])
    preco=float(lista[2])
    total+=preco*quantidade

print(total)
    
    
    