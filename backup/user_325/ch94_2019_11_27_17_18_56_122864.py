velocidade = int(input("Velocidade máxima da via em km/h "))
distancia = int(input("Distância entre as cameras em metros "))
placa_tem = True

while placa_tem:
    
    placa = input("Digite a placa do veículo ")
    tempo1 = float(input("Digite o tempo que passou na primeira camera "))
    tempo2 = float(input("Digite o tempo que passou pela segunda camera "))
    if len(placa)>= 0:
        if distancia/(tempo2-tempo1) >= velocidade*1.5:
            print("Infração GRAVÍSSIMA! - você foi multado em R$ 586,29")
        
        elif distancia/(tempo2-tempo1) > velocidade*1.2 and distancia/(tempo2-tempo1) < velocidade*1.5:
            print("Infração GRAVE! - você foi multado em R$ 195,23")
        
        elif distancia/(tempo2-tempo1) <= velocidade*1.2:
            print("Não foi multado")
        
        else:
            print("Infração MEDIA! - você foi multado em R$ 130,16")
    else:
        break
else:
    placa_tem == False