a= input('Código está executando(s/n)? ')
b= input('Produz o resultado correto?(n/s) ')
if a == 'n':
    print('Corrija o código e tente de novo')
else:
    print(b)
    if b == 's':
        print('Parabéns!')
    if b == 'n':
        print('Corrija o código e tente de novo')
return a
        
    