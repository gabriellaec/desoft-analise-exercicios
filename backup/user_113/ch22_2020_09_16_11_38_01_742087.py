cig_dia = int(input('Quantos cigarros fuma por dia?: '))
anos = int(input('A quantos anos vc fuma?: '))
tempo = (cig_dia * 0.00694444) * (365*anos)
print(tempo)