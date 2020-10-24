#Calcular a velocidade média de um veículo, recebendo distância, em km, e tempo gasto, em horas

def calcula_velocidade_média(distância, tempo):
    y = distância/tempo
    return y
a = 30
b = 3
c = calcula_velocidade_média(a, b)
print('A velocidade média do veículo percorrendo a distância {0}km em {1}h é {2}km/h'. format(a, b, c));