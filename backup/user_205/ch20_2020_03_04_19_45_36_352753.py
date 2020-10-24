distancia = float(input("Qual a distancia que você quer percorrer: "))
if distancia < 200:
    print ("Preço da passagem é {0:.2f}".format(distancia*0.5)
else:
    print ("Preço da passagem é {0:.2f}".format(distancia*0.5 + 0.45*distancia)