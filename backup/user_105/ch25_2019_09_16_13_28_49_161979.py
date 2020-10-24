distancia = float(input('Quantos km você pretende percorrer?: '))
def preço_pago(preço):
    if distancia <= 200:
        return distancia*(1/2)
    else:
        return 100 + (distancia-200)*(9/20)
print('o valor é:{0:.2f} '.format(preço_pago(distancia)))


