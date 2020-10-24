def tempo (d, f):
    t = d*f*10
    return t


dia = int(input("quantos cigarros vc fuma por dia?" ))
anos = int(input("E a quantos anos vc fuma?" ))

tempo_perdido = tempo(dia, anos)
print (tempo_perdido)