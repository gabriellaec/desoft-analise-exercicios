def velocidade(valor):
    if valor<=80:
        print('Não foi multado')
    elif valor>80:
        resultado= (valor-80)*5
        return ('você foi multado em {0:.2f}.'.format(resultado))
w= int(input('Quantos km/h você estava?' ))
print(velocidade(valor))