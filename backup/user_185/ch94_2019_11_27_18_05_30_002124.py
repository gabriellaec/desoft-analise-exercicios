velocidade = int(input("Digite uma velocidade: "))
dist = int(input("Digite a distancia entra as duas câmeras: "))

carros = {
        }

segundo_radar = {
        }

program_start = "True"

while program_start == "True":
    
    lista_keys = list(carros.keys())
    
    placa = input("Digite a placa: ")
    
    if placa == "":
        break
    
    if placa not in lista_keys:
        radar_1 = int(input("Digite o tempo do primeiro radar: "))
    
    if placa in lista_keys:
        
        radar_2 = int(input("Digite o tempo do segundo radar: "))
        
        dif_tempo = radar_2 - radar_1
        
        vel_carro = dist / dif_tempo
        
        converte = vel_carro * 3.6
        
        segundo_radar[placa] = converte
        
        if converte > velocidade and converte <= velocidade*1.2:
            print("Por ter atingido a velocidade {0}, o motorista cujo carro tem placa {1} foi multado em R$ 130,16".format(converte, placa))
            
        elif converte > velocidade*1.2 and converte <= velocidade*1.5:
            print("Por ter atingido a velocidade {0}, o motorista cujo carro tem placa {1} foi multado em R$ 195,23".format(converte, placa))
            
        elif converte > velocidade*1.5:
            print("Por ter atingido a velocidade {0}, o motoristsa cujo carro tem placa {1} foi mutlado em R$ 585,69".format(converte, placa))
            
    
    
    
    carros[placa] = radar_1
    
    #lista_placas.append(placa)
#    if pergunta == "Não":
#        program_start = False

print(carros)
print(lista_keys)
print(segundo_radar)