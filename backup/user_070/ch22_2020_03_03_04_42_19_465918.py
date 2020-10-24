def tempo_de_vida_fumante(a,b):
    x=(365*b)*a
    y=x*10
    z=(y/60)/24
    return z

pd=int(input('Quantos cigarros por dia? '))
a=int(input('Faz quanto tempo? '))

tempo=tempo_de_vida_fumante(pd,a)
print(tempo)