km = int(input('Qual a distancia percorrida em quilometros? '))
def valor_corrida(km):
    if km <= 200:
        p = 0.5 * km
        return p
    else:
        p = 0.5*200.0 + (km - 200.0)*0.45
        return p

preco = valor_corrida(km)
print ("O valor da corrida foi: {0:.2f}". format (preco))