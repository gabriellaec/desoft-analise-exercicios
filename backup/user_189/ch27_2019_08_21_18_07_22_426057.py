print ("hello world")
def f():

    x = 1+(1/2)+(1/2**2)+(1/2**3)
    a=(3*4+5)/(1+2*3)
    c=(3**2+4**2)**(1/2)
    return x,a,c

print (f())
    
tamanho=100
expoente=1
soma=1
for i in range(tamanho):
    soma=soma+(1/2**expoente)
    expoente+=1
print(soma)
a="cacete"
b="nem sei mano"
c="mas q carajos"
print('eu gosto de batatas e {0}, com {1},kkk {2}'.format(a,b,c))

print ('meu sono está forte demais, alguem por favor me tira daqui')