vm=int(input('Qual a velocidade: '))
if vm>80:
    print(f'Você foi multado em {(vm-80)*5} reais')
else:
    print(f'Você não foi multado')