def calcula_posicao(t,s0,v):
    s= s0 + v*t
    return s

x=1
y=4
z=2
w=calcula_posicao(x,y,z)
print(w)