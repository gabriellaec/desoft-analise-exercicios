arquivo = open('dados.csv')

linhas = []

for linha in arquivo:
    
    linhas.append(linha.split(','))
    
print(linhas)