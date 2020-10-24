def aniversariantes_de_setembro(nivers):
    setembrinos={}
    for pessoas,aniversarios in nivers.items():
        if aniversarios[3:5]== '09':
            setembrinos[pessoas]= aniversarios
    return setembrinos
            
            