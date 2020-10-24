a=float(input('Qual será a distância percorrida ? '))
def preco_passagem(a):
    if a<=200:
        return a*0.5
    else:
        return 100+(a-100)*0.45
print('{0:.2f}'.format(preco_passagem(a)))