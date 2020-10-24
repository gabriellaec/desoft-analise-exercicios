import csv
custo = 0
with open('churras.txt')as lista:
    consumo = csv.reader(lista)
    for i in consumo:
        quant=float(i[1])
        preco=float(i[2])
        custo+=quant*preco
        
print(custo)
 
                
