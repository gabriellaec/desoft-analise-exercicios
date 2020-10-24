def velocidade(valor):
    if valor<=80:
        print('Não foi multado')
    else:
        valor= (valor-80)*5
        return ('você foi multado em {0:.2f}.'.format(valor))
w= int(input('Quantos km/h você estava? )
print(velocidade(valor))