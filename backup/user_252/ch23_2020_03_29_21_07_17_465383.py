velocidade=(input('qual a velocidade: '))
def f(v):
    if v > 80:
        y=(v-80)*5
        return y
    else:
         input('Não foi multado')

y=f(velocidade)
print(f 'você foi multado, preço: {y:.2f}')