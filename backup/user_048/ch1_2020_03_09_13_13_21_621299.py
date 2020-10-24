def calcula_valor_definido(v,n,t):
    y =v*(1+t)**n
    return y
v=1000
n=10
t=0.1
print(calcula_valor_definido(v,n,t))