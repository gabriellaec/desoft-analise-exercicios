def cust_viagem(km1):
    if km1<=200:
        cost=km1*0.5
    else:
        km=200
        custo=(km1-km)*0.45
        cost=custo+100
    return cost

km1=int(input('Quantos kilômetros você deseja viajar? '))
print('Sua viagem custará {} reais!'.format(cust_viagem(km1)))