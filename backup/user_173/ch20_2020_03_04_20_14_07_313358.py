distancia = float(input('Escreva a distância que você quer percorrer em km'))
if distancia <= 200:
    valor = 0.5*distancia
else:
    valor = (0.45*distancia) + 100
    
    
print '{:.2f}'.format(valor)