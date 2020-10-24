velmax = float(input('Qual a velocidade máxima da via (em km/h)? '))
cam_distancia = float(input('Qual a distância entre as duas câmeras? (em metros) '))

radar = True
tempo = 0
origem = 0
final = cam_distancia

multam = 130.16
multag = 195.23
multagg = 3*multag

carros = {
    #O dicionário possui a seguinte estrutura
    #"aaaaaaa": [cameras, tempoinicial, tempofinal, velocidade, infracao, multa]
}

while radar:
    tempo += 1

    placa = input("Qual a placa?")
    while len(placa) != 7:
        if placa == '[]': #Vazio
            radar = False
        else:
            placa = input("Qual a placa?")

    if placa not in carros:
        carros[placa] = [0]*6
        carros[placa][0] = 1 #Qual camera já passou
        carros[placa][1] = tempo

    elif placa in carros:
        carros[placa][2] = tempo
        deltat = carros[placa][2] - carros[placa][1]
        vel = cam_distancia/deltat
        velkmh = vel * 3.6 #Convertendo m/s para km/h
        carros[placa][3] = velkmh
        #Verifica se o cara tomou multa
        if velkmh>velmax and velkmh<=(velmax*1.2):
            carros[placa][4] = "Infração média"
            carros[placa][5] = "Penalidade: Multa de R${}".format(multam)

        elif velkmh<=(vel*1.2) and velkmh<=(velmax*1.5):
            carros[placa][4] = "Infração grave"
            carros[placa][5] = "Penalidade: Multa de R${}".format(multag)

        elif velkmh > (velmax*1.5):
            carros[placa][4] = "Infração gravíssima"
            carros[placa][5] = "Penalidade: Multa de R${} ; suspensão imediata do direito de dirigir e apreensão do documento de habilitação".format(multagg)

    print (carros)