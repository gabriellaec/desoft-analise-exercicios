vel_max = int(input("Qual a velocidade máxima da via (km/h)? "))
dis_cam = int(input("Qual a distância entre as câmeras (metros)?"))
i = 0
while i == 0:
    placa = input("Qual a placa do veículo (XXXXXXX)? ")
    while placa != (""):
        instante1 = int(input("Passou pela câmera 1 em qual instante (segundos)?"))
        instante2 = int(input("Passou pela câmera 2 em qual instante (segundos)?"))
        vel_media = dis_cam/(instante2 - instante1) #m/s
        vel_media_final = vel_media * 3.6 #km/h
        if vel_media_final <= vel_max:
            print("Está dentro do limite")
        else:
            if vel_media_final > vel_max and vel_media_final <= vel_max * 1.2:
                print("Infração Média. Multa de R$ 130,16")
            if  vel_media_final > vel_max and vel_media_final > vel_max * 1.2 and vel_media_final <= vel_max*1.5:
                print("Infração Grave. Multa de R$195.23")
            if vel_media_final > vel_max and vel_media_final > 1.5*vel_max:
                print("Infração Gravíssima. Multa de R$585,69, além da suspensão do direito de dirigir e apreensão da carteira")
    break
    