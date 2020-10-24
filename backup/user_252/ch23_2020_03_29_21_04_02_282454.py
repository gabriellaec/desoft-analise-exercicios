velocidade=(input('qual a velocidade: '))
def p(v):
    if v > 80:
        y=(v-80)*5
        return y
    else:
         input('Não foi multado')

y=p(velocidade)
print('você foi multado, preço: {0:2f}')