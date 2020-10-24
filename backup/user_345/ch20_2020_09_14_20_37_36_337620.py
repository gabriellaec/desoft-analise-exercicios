def valor_corrida(km):
    if km <= 200:
        p = 0.5 * km
        return p
    else:
        p = 0.45 * km
        return p

x = int(input('Qual a distancia percorrida em quilometros? '))
print (valor_corrida(x:.2ft))