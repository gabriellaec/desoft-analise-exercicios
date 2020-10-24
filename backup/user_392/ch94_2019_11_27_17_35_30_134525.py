VIDA = True

vel_max = float(input('qual é a velocidade maxima?? '))
d_cam = float(input('qual é a distancia entre as cameras? '))

while VIDA:
    placa = input('digite uma placa: ')
    lista_placa = list(placa)
    print(len(lista_placa))
    
    if len(lista_placa) == 0:
        print('placa inválida, rode de novo o programa')
        VIDA = False
        break
    if not len(lista_placa) == 7 :
        print('PLACA INVALIDA!')
   
    
    else:
        tempo = int(input('digite um instante: '))
        
        placa_ = input('digite uma placa: ')
        lista_placa_ = list(placa_)
        if len(lista_placa_) == 0:
            print('placa inválida, rode de novo o programa')
            VIDA = False
            break 
        
        tempo_ = int(input('digite um instante: '))

        if lista_placa == lista_placa_:
            d_tempo = tempo_ - tempo
            velocidade = d_cam/d_tempo
        
            if velocidade <= vel_max+(vel_max*0.2) and velocidade >= vel_max:
                print('infração média')
                penalidade = 130.16
                print(' a multa é de {0}R$'.format(penalidade))
                
            elif velocidade >= vel_max+(vel_max*0.2) and velocidade <= vel_max+(vel_max*0.5):
                print('infração grave')
                penalidade = 195.23
                print(' a multa é de {0}R$'.format(penalidade))
        
            elif velocidade >= vel_max+(vel_max*0.5):
                print('infração gravissima')
                penalidade = 195.23*3
                print('apreenção da habilitação e multa de {0}R$'.format(penalidade))
            
            else:
                print ('nada a ser pronunciado')
