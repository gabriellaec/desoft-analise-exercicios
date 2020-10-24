distancia = float(input("Digite a distância a percorrer: "))
if (distancia <= 200):
    total = 0.5 * (distancia)
    print('o total é igual a {0:.2f}'.format(total))
else:
    total = 0.45 * (distancia)
    print('o total é igual a {0:.2f}'.format(total))