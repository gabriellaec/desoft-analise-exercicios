x = int(input('Quantos cigarros você otário fuma por dia?'))
y = int(input('Há quantos anos fuma?'))

def otario_fumante(a,b):
    x=b*365 #Tempo em dias que ele fumou
    y=a*10/1440
    z=x*y
    return z
print(otario_fumante(x,y))