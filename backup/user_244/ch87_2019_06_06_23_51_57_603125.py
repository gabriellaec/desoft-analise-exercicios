import csv
custo = 0  
with open('churras.txt','r') as churras:
    texto = csv.reader(churras)
   
	for i in texto:
    	quant = float(i[1])
    	preco = float(i[2])
    	custo += quant*preco
    
print(custo)