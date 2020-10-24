velo = float(input('Digite sua velocidade: '))
if velo > 80:
    multa = (velo - 80) * 5
    print(f'Você foi multado R${multa:.02f}')
else:
    print('Não foi multado')