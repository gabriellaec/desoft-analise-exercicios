def reducao_na_vida(d):
    tempo=((n*10)/60/24)
    return tempo
n=int(input('numero de cigarros'))
dias=reducao_na_vida(n)
print('voce tem {0} dias a menos'.format(dias))