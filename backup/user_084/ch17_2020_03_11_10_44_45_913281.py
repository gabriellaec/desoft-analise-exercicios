def eh_bissexto(x):
x=int(input('escolha um ano: '))
if x<=0:
    return('esse ano nao existe')
elif x%4==0:
    return('esse ano é bissexto')
else:
    return('ano nao bissexto')
