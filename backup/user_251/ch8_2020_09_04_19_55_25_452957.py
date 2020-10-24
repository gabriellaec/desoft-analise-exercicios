def calcula_posicao(t,s0,v):
    s = s0 + (v*t)
    return s

a = 2
b = 5
c = 25
resultado = calcula_posicao(a,b,c)

print(resultado)