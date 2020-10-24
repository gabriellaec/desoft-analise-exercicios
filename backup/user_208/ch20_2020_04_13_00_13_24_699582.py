distancia = int(input("Quantos quilometros você vai percorrer? "))
passagem_200km = distancia*0.5
passagem_alem_200km = distancia*0.5 + (distancia-200)*0.45
if distancia <= 200:
    print ("O valor da passagem será de {0.:2f}!".format(passagem_200km))
else:
    print ("O valor da passagem será de {0.:2f}!".format(passagem_alem_200km))


                