vmax= int (input('Velocidade maxima:   '))
dist= int (input('Distancia à percorrer:   '))
placa= []
tempo= []
while True:
    pla= str (input('Qual a placa do carro (7digitos):   '))
    placa.append(pla)
    if (len(pla)) != 7:
        print('Placa invalida')
    else:
        if pla == '':
            print('fim')
            break
    inst= int(input('Qual o instante:   '))
    tempo.append(inst)
inst