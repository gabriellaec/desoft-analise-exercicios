import csv
custo = 0
with open('churras.txt','r') as arquivo:
    consumo = csv.reader(arquivo)
    for coluna in consumo:
        quant = int(coluna[1])
        preco = float(coluna[2])
        custo+= quant*preco
print(custo)
                             