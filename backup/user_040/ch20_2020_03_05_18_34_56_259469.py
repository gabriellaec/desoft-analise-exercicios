distancia=float(input("Qual distância você deseja percorrer: "))
if (distancia<=200):
    print ("R$",(distancia*0.5):.2f)
else:
    print ("R$",(200*0.5+(distancia-200)*0.45):.2f)