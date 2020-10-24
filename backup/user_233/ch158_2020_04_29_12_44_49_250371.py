arquivo = open('texto.txt')

contagem = 0

for linha in arquivo:
    contagem += len(linha.split(' '))
    
print(contagem)

arquivo.close()