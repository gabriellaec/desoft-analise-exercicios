import csv
custo = 0
with open ('churras.txt','r') as cons:
    cons = churras.readlines()
    for row in cons:
        quant = float(row[1])
        preco = float(row[2])
        custo += quant*preco
        
print(custo)
   
    

