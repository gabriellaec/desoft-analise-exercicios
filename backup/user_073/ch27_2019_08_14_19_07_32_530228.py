def reducao_na_vida(n,y):
    tempo=((n*10)/60/24)*y*365
    return tempo
n=int(input('numero de cigarros por dia'))
y=int(input('ha quantos anos vc fuma'))
dias=reducao_na_vida(n,y)
print('voce tem {0} dias a menos de vida'.format(dias))