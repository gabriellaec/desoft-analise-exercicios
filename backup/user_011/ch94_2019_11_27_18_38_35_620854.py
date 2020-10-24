vel_via = int(input('Qual a velocidade máxima da via?'))
d_cameras = int(input('Qual a distância entre as câmeras?'))

placa = 0

placal = []
tempol = []

i = 0

while placa != str(''):
    placa = input('qual a sua placa?')
    tempo = int(input('tempo?'))
    
    placal.append(placa)
    
    for placa in placal:
        
        if placa in placal:
            
            tempo2 = int(input('tempo?'))
        
            vel = d_cameras/abs(tempo2-tempo)
        
            if vel > vel_via and vel < vel_via*1.2:
                print('infracao media')
            elif vel > vel_via*1.2 and vel < vel_via*1.5:
                print("infraçao grave")
            
            else:
                print('infracao gravissima')