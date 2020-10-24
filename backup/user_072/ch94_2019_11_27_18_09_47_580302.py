v_max = input(int('Qual a velocidade maxima da via em Km/h ?'))
dist = input(int('Qual a distancia entre as cameras em metros ?'))
placa = input('Qual a placa do carro ?')
while placa == placa:
    ti = input(int('Qual o instante em que o carro passa pela primeira camera em segundos ?'))
    placax = input('Qual a placa do carro ?')

    if dist/(tf-ti) <= 0.2*v_max:
        return 