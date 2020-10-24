a= int (input ('Quantos cigarros você fuma por dia? '))
b= int (input ('Há quantos anos você fuma? '))

def h(a,b):
    y=((a*10)/1440)+10*(365*a*b)/1440
    return y
dias_perdidos=h(a,b)
print (dias_perdidos)