cigarros= int(input('Quantidae de cigarros fumados por dia: '))
anos= int(input('Anos que fuma: '))
dias= anos * 365
quant= (cigarros * dias)
life= (quant * 10)/ 24
print(f'Vc perdeu {life} minutos de vida')
