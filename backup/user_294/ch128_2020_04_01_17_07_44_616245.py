esta_se_movendo = True
if esta_se_movendo:
    resposta1 = input("esta se movendo?: ")
    if resposta1 == 's':
        resposta2 = input("deveria se mover?: ")
        if resposta2 == 's':
            print ('Sem problemas!')
        else:
            print ('Silver Tape')
    else:
        resposta3= input ("deveria estar parado?: ")
        if resposta3 == 's':
            print ('Sem problemas!')
        else:
            print ('WD-40')
                              