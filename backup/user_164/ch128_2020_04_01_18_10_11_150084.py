sim = ["sim"]
nao = ["nao"]

esta_se_movendo = input ("Está se movendo?")
if esta_se_movendo in sim:
    se_move = input ("Deveria se mover?")
    if se_move in sim:
        print ("Sem problemas!")
    elif se_move in nao:
        print ("Silver Tape")
    else:
        print ("Digite uma resposta valida")
if esta_se_movendo in nao: 
    nao_se_move = input ("Derveria se mover ?")
    if esta_se_movendo in sim:
        print ("Sem problemas!")
    elif esta_se_movendo in nao:
        print ("Usar WD-40")
    else:
        print ("Digite uma resposta valida")