a=int(input("Quantos cigarros fuma por dia?"))
b=int(input("Há quantos anos fuma?"))
def soma(a, b):
    t=(a*(10/1440))*(b*365)
    return t
t=soma(a, b)
print(a, b, t)
