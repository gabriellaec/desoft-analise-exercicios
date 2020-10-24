import csv
custo = 0
with open ('churras.txt','r') as cons:
    cons1 = cons.readlines()
    for row in cons1:
        quant = float(row[1])
        preco = float(row[2])
        custo += quant*preco
        
print(custo)
   
    

