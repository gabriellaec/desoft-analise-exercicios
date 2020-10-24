import time
carro = True
distance = int(input("Distance:"))
speed = int(input("Velocidade:"))
while carro == True:
    placa_carro = input("Placa Carro:")
    time1 = time.time()
    if placa_carro == "":
        carro = False
        break
    Placa2 = input("Placa Carro:")
    if placa_carro == Placa2:
        time2 = time.time()
    tot = time2 - time1
    speed2 = distance/tot
    if speed2 == speed*1.2 or speed2 > speed and speed2 < (speed*1.21):
        print("Multa: Infracao Media")
        print("Penalidade: 130.16")
    elif speed2 > speed*1.2 and speed2 < (speed*1.5):
        print("Multa: Infracao Grave")
        print("Penalidade: 195.23")
    elif speed2 > speed*1.5:
        print("Multa: Infracao Gravissima")
        print("Penalidade: 3*195.23 e suspensao imediata da CNH")
