distancia = float(input("Digite a distância a percorrer: "))
if (distancia <= 200):
    total = 0.5 * (distancia)
    print('o total é igual a R${0:.2f}'.format(total))
elif(distancia>200):
    total = 0.5*200+0.45 * (distancia-200)
    print('o total é igual a R${0:.2f}'.format(total))