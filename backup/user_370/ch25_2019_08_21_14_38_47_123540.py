distancia=int(input('Quantos km voce percorreu?'))
def distancia_km (x):
    if x<= 200:
        return float("{0:.2f}".format(0.50*x))
    elif x>200:
        return float("{0:.2f}".format(100+0.45*(x-200)))
   
                     
print(distancia_km(distancia))
    
    