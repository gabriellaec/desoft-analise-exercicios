distancia = int(input( 'Quantos km voce percorre ? '))
def quantidade_km (x):
    if x<=200 :
    	return x*0.5
    else:
    	return x*0.45
print (quantidade_km(distancia))
