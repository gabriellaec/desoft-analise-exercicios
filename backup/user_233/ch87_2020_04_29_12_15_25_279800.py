arquivo = open('churras.txt')

valor = 0

for linha in arquivo:
    
    linha = linha.split(',')
    valor += float(linha[1]) * float(linha[2])

arquivo.close()

print(valor)