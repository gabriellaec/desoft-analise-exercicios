velocidade=float(input('Qual a velocidade: '))
def f(v):
    if v>80:
        y=(v-80)*5
        return y
    else:
        input('Nao foi multado')
y=f(velocidade)
print('{0:2f}'.format(y))