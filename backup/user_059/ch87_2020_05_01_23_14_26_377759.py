import csv

with open('churras.txt', 'r') as arquivo:
    conteudo = csv.DictReader(arquivo)
    
x = list(conteudo)
soma = 0 

for i in range(len(x)):
    y = x[i][1]* x[i][2]   
    soma += y

print(soma)
