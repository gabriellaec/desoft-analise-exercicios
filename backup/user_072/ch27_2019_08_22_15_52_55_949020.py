a=int(input('Quantos cigarros voce fuma por dia ? '))
b=int(input('Há quantos anos voce fuma ? '))
def anos_perdidos(a,b):
    y=a*b*365*10/(60*24)
    return y
print(anos_perdidos(a,b))