a = int(input('Digite um numero: '))
b = int(input('Digite um segundo numero:'))

c = True

while c:
    x = int(input('Deseja o resultado da soma ? 0 - Sim 1 - Não'))
    if x != 0:
        print('Tente novamente')
    else:
        print(a+b)
        c = False