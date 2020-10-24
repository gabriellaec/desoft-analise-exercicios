velocidade=int(input('qual a velocidade: '))
def f(v):
    if v>80:
        y=(v-80)*5
        return y
    else:
         input('Não foi multado')

y=f(velocidade)
print('você foi multado, prelço: {0:2f}'.format(y))