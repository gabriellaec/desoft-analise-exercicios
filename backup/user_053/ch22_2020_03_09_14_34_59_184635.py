a=int(input('Há quantos anos você fuma? '))
b=int(input('Quantos cigarros por dia você fuma? '))

def tempo_perdido(dias,cigarros):
    reducao=(10/(60*24))*365*dias*cigarros
    return reducao

x=a
y=b
z=tempo_perdido(x,y)
print(z)