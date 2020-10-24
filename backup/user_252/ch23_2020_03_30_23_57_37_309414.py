velocidade=input('qual a velocidade: ')
def f(v):
    if 80<v:
        y=(v-80)*5
        return y
    else:
         input('Não foi multado')

y=f(velocidade)
print('{0:2f}'.format(y))