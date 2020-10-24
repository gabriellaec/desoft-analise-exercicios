km = int (input ("Qual distancia que voce quer percorrer?" ))


if km <= 200:
    preco = km *0.5
    
else: 
    preco = 200 * 0.5 + (0.45 * (km-200))
    
print ("O preço da passagem vai ser de {0:.2f} reais" .format (preco))