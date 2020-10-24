
velocidade_max = 100
print (velocidade_max)
vel_inicial = int(input('velocidade passando pela camera 1: '))
vel_final = int(input('velocidade passando pela camera 2: '))
placa = input('qual a placa registrada: ')
distancia_cameras = int(input('distancia entre as cameras em metros: '))

def multa(vel_inicial,vel_final,placa,distancia_cameras):
    velocidade_media = (vel_inicial + vel_final) / 2
    if  100 < velocidade_media > 120 :
        print ('infracao media, multa de 130,16 reais')
    elif  120 < velocidade_media > 150 :
        print ('infracao grave, multa de 195,23 reais')
    elif  velocidade_media > 150:
        print ('infracao gravissima , multa de 3 vezes 195,23 reais e apreensao do doc. de habilitacao')
    return multa
