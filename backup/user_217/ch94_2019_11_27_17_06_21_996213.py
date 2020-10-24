velocidade=int(input("Velocidade da via?: "))
distancia_das_cameras=int(input("Distancia das cameras?: "))

running = True 
while running:
    
    placa = input("Qual é a placa?: ")
    instante = int(input('Qual o instante de tempo?: '))
    
    if distancia_das_cameras/instante > 0.2*velocidade:
        print(placa,'','infração media','multa R$ 130,16')
    
    if 0.2*velocidade < distancia_das_cameras/instante <= 0.5*velocidade:
        print(placa,'','infração grave','multa R$ 195,23')
        
    if distancia_das_cameras/instante > 0.5*velocidade:
        print(placa,'','infração gravissima','multa R$ ',3*195.23)
    
    if distancia_das_cameras/instante <= 0.2*velocidade:
        print(placa,'Sem multa')

    if placa == '':
        break