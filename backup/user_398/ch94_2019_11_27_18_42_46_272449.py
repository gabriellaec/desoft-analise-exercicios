vmax = float(input('Velocidade máxima(km/h):'))
dist = float(input('Distância entre as câmeras(m):'))

loop = True

lista_placas=[]
lista_instantes=[]

while loop == True:
    
    
    placa = str(input('Placa do veículo:'))
    
    if placa == " ":
        break
    
    instante = float(input('Instante do veículo(s):'))
    
    
    i=0
    while i<len(lista_placas):
        if placa == lista_placas[i]:
            vel = dist/abs(instante-lista_instantes[i])
            if vel>vmax/3.6 and vel<=1.2*vmax/3.6:
                print('Placa:',placa)
                print('velocidade(km/h):',vel*3.6)
                print('{0} passou da velocidade. Infração média'.format(placa))
                print('Multa de R$ 130,16')
                break
            elif vel>1.2*vmax/3.6 and vel<=1.5*vmax/3.6:
                print('Placa:',placa)
                print('velocidade(km/h):',vel*3.6)
                print('{0} passou da velocidade. Infração grave'.format(placa))
                print('Multa de R$ 195,23')
                break
            elif vel>1.5*vmax/3.6:
                print('Placa:',placa)
                print('velocidade(km/h):',vel*3.6)
                print('{0} passou da velocidade. Infração gravíssima'.format(placa))
                print('Multa de R$ 585,69')
                print('Suspensão ido direito de dirigir e apreensão do documento de habilitação')
                break
            else:
                print('Placa:',placa)
                print('velocidade(km/h):',vel)
                print('Não passou da velocidade máxima')
                break
        i+=1
                
    
    lista_placas.append(placa)
    lista_instantes.append(instante)
    