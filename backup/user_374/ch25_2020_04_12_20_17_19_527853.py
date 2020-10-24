import math
def jaca(v,teta):
    
    calculo = ((v**2)*2*math.sin(teta)*math.cos(teta))/9.8
    
    if calculo == 100:
        return 'Acertou!'
    elif calculo > 102:
        return 'Muito longe'
    elif calculo < 98:
        return 'Muito perto'