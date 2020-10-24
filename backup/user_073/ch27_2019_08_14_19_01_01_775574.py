def reducao_na_vida(d):
    tempo=((n*10)/60/24)*y
    return tempo
n=int(input('numero de cigarros por dia'))
y=int(input('ha quantos anos vc fuma'))
dias=reducao_na_vida(n)
print('voce tem {0} dias a menos'.format(dias))