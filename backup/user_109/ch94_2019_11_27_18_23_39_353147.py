import random


def Calcula_penalidade(tempo1, tempo2, velocidade_via, distancia_cameras):
    multa = 0
    velocidade_carro = distancia_cameras/(tempo2-tempo1)
    if velocidade_carro < velocidade_via:
        multa = 'Você não recebeu nenhuma penalidade'
    elif velocidade_via < velocidade_carro <= velocidade_via*1.2:
        multa = 130.16
    elif velocidade_via*1.2 < velocidade_carro <= velocidade_via*1.5:
        multa  = 195.23
    elif velocidade_via*1.5 < velocidade_carro:
        multa = 3*195.23

    return multa


velocidade_via = float(input("Qual é a velocidade máxima da via [m/s]?"))
distancia_cameras = float(input("Qual é a distância entre as duas câmeras?"))

carro1 = ['abc-1234', random.randint(0,8), random.randint(15,30)]
carro2 = ['cde-4567', random.randint(0,8), random.randint(15,30)]
carro3 = ['fgh-9101',random.randint(0,8), random.randint(15,30)]
carros = [carro1, carro2, carro3]

for i in range(len(carros)):
    if carros[i][0] == 'abc-1234':
        penalidade = Calcula_penalidade(carros[i][1], carros[i][2], velocidade_via, distancia_cameras)
        print('{}:{}'.format(carros[i][0], penalidade))
    elif carros[i][0] == 'cde-4567':
        penalidade = Calcula_penalidade(carros[i][1], carros[i][2], velocidade_via, distancia_cameras)
        print('{}:{}'.format(carros[i][0], penalidade))
    elif carros[i][0] == 'fgh-9101':
        penalidade = Calcula_penalidade(carros[i][1], carros[i][2], velocidade_via, distancia_cameras)
        print('{}:{}'.format(carros[i][0], penalidade))