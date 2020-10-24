km = int(input('Qual a distancia percorrida em quilometros? '))
def valor_corrida(km):
    if km <= 200:
        p = 0.5 * km
        print (p)
    else:
        p = 0.5*200.0 + (km - 200.0)*0.45
        print (p)
