a= int (input ('Quantos cigarros você fuma por dia? '))
b= int (input ('Há quantos anos você fuma? '))

def h(a,b):
    y=((a*10)*365*a*b)/60
    return y
dias_perdidos=h(a,b)
print (dias_perdidos)