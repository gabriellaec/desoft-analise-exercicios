distancia=int(input("Qual a distância em km?"))
if distancia<=200:
    print("O preço é: R${0:.2f}".format(distancia*0.5))
else:
    print("O preço é: R${0:.2f}".format(200*0.5+0.45*(distancia-200)))

