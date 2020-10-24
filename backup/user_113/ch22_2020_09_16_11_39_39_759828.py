cig_dia = int(input('Quantos cigarros fuma por dia?: '))
anos = int(input('A quantos anos vc fuma?: '))
tempo = (((cig_dia * 10)/60)/24) * (365*anos)
print(tempo)