def calcula_posicao(So,t,v):
    s=So + v * t
    return s

So=0
t=10
v=5
y= calcula_posicao(So,t,v)
print(y)