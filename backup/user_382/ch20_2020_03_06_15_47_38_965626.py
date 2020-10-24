qnto_km = float(input('Qual a distancia que deseja percorrer?'))
	
    if qnto_km <=200:
        total = qnto_km*0.5 
    else:
        total = 200*0.50 + (qnto_km-200)*0.45
        
print (total)