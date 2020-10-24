distancia=float(input("Qual distância você deseja percorrer: "))
if (distancia<=200):
    print ("R$",(distancia:.2f*0.5))
else:
    print ("R$",(200*0.5+(distancia:.2f-200)*0.45))