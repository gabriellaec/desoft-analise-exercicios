v = int(input('Qual a velocidade máxima da via(km/h)? '))
d = int(input('Qual a distancia entre as câmeras(m)? '))
ms = v/(3.6)

running = True
while running:
    
    placa = input('Qual a placa do veículo? ')
    if len(placa) < 1:
        break
    while len(placa) != 7:
        placa = input('Favor digitar placa corretamente ')
        
    inst1 = int(input('Em que momento o veículo passa pela primeira câmera? '))
    inst2 = int(input('Em que momento o veículo passa pela segunda câmera? '))
    c = d/(inst2 - inst1)
    
    if c <= ms:
        print('Sem infração')
    elif c <= ms + ms*0.2:
        print('Infração média, punição aplicada de R$ 130,16')
    elif c <= ms + ms*0.5:
        print('Infração grave, punição aplicada de R$ 195,23')
    elif c > ms + ms*0.5:
        print('Infração gravíssima, punição aplicada de R$ 195,23 x 3 e suspensão imediata do direito de dirigir e apreesão da habilitação')