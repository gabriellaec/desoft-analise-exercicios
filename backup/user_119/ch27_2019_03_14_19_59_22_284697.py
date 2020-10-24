c=int(input('cigarros por dia?'))
a=int(input('quantos anos?'))
def tempo_vida(c,a):
    y=c*1/144*365*a
    return y
print(tempo_vida(c,a))