a = input('Qual o valor da sua conta, em reais?: ')
b = input('Qual o valor da sua conta, em centavos?: ')
c = input('Qual o valor da sua conta, em decimos de centavos?: ')

texto= 'Valor da conta com 10%: R$ {0}.{1}{2}'.format(a,b,c)

print(texto)