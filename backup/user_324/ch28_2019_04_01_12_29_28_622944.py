v=float(input('qual a velocidade: '))
if v>80:
    multa=(v-80)*5
    print(format(multa,'.2f'))
else:
    print('não foi multado')