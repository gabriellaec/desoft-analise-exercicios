distancia = float(input("Qual distância você deseja percorrer: "))
if (distancia<=200):
    print ("R${0:.2f}".format(distancia*0.5))
else:
    print ("R${0:.2f}".format((distancia-200)*0.45))