import csv
custo=0
with open('churras.txt') as churras:
    consumo=csv.reader(churras)
    for b in consumo:
        quant=float(b[1])
        valor=float(b[2])
        custo+=quant*valor
print(custo)
            
                
            	
         
                
        
	