distancia = float(input('Quantos km você pretende percorrer?: '))
def preço_pago(preço):
    if distancia <= 200:
        return distancia*(1/2)
    else:
        return distancia*(9/20)
print('o valor é:{0} '.format(preço_pago(distancia)))


