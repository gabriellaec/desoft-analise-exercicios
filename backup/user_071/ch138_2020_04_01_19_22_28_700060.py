resposta_final = 'n'
while resposta_final != 's':
    executando = input("o programa está funcionando? (s/n) ")
    if executando == 'n':
        print('Corrija o código e tente de novo')
    elif executando == 's':
        resultado = input('o codigo produz o resultado correto?(s/n) ')
        if resultado == 'n':
            print('Corrija o código e tente de novo')
        elif resultado == 's':
            resposta_final = 's'
print('Parabens!')