resposta=int(input('qual sua velocidade?'))
if resposta>=80:
    multa=(resposta-80)*5
    texto='voce foi multado em {0:.2f} reais'.format(multa)
    print(texto)
else:
    print('Não foi multado')