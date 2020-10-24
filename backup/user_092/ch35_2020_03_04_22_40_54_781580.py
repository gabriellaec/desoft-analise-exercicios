num = soma = 0
num = int(input('digite numeros[0 para parar]'))
while(num!=0):
    soma += num
    num = int(input('digite numeros[0 para parar]'))
print('a soma deles foi {0}'.format(soma))