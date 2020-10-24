distancia = float(input("Qual a distancia que você quer percorrer: "))
if (distancia <= 200):
    print ("O  preço da passagem é R$ {0:.2f}".format(distancia*0.5))
else:
    print ("O preço da passagem é R$ {0:.2f}".format(distancia*0.45))
    
   