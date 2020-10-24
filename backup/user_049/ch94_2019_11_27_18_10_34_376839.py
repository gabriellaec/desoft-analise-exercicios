distancia = int(input("Qual a distância entre as câmeras? "))
v_max = int(input("Qual a velocidade máxima permitida na rodovia? "))
v_max = v_max/3.6


sistema = True
while sistema:
    placa = input("Qual a placa do veículo? ")
    if placa == "":
        sistema = False 
    tempo = int(input("Quanto tempo ele levou para chegar de uma câmera e a outra? "))

    print(v_max)
    v_media = distancia/tempo
    
    if v_media <= v_max:
        print('')
        print('Parabéns você não infringuiu a velocidade máxima permitida.')
        print('Continue assim!')

    if v_media > v_max and v_media <= 1.2*v_max:
        print('')
        print('A infração do carro de placa {0} é :'.format(placa))
        print('- Infração média.')
        print('- Sua multa é de R$ 130,16.')
        
    if v_media > 1.2*v_max and v_media <= 1.5*v_max:
        print('')
        print('A infração do carro de placa {0} é :'.format(placa))
        print('- Infração grave.')
        print('- Sua multa é de R$ 195,23.')
        
    if v_media > 1.5*v_max:
        print('')
        print('- A infração do carro de placa {0} é :'.format(placa))
        print('- Infração gravíssima.')
        print('- Suspensão Imediata + Apreensão do Documento de Habilitação.')
        print('- Sua multa é de 3 x R$ 195,23.')