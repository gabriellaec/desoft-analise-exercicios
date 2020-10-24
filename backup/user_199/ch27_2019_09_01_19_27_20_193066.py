d=int(input('quantos cigarros vc fuma por dia?: '))
a=int(input('a quantos anos vc fuma?: '))

def dias_perdidos(d,a):
    y = ((365*a)*d)*10/1440
    return y
print(dias_perdidos(d,a))