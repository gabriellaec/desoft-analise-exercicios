km = int (input ("Qual distancia que voce quer percorrer?" ))


if km > 200:
    preco = 200 *0.5 + (km-200)*0.95
    
else: 
    preco = km * 0.5 
    
print ("O preço da viagem vai ser de {0:2f} reais" .format (preco))