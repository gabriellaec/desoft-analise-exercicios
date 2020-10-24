km = int (input ("Qual distancia que voce quer percorrer?" ))


if km <= 200:
    preco = km *0.5
    
else: 
    preco = km * 0.5 + (0.95 * km)
    
print ("O preço da viagem vai ser de {0:.2f} reais" .format (preco))