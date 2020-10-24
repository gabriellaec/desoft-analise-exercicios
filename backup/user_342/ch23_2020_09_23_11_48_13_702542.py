resposta=int(input('qual_sua_velocidade?'))
if resposta>=80:
    print('voce foi multado')
    multa=(resposta-80)*5
    print(multa:.2f)
else:
    print('Não foi multado')