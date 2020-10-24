while True:
    x = input('Código está executando? ')
    if x =='n':
        print("Corrija o código e tente de novo")
    elif x=='s':
        y = input('Produz o resultado correto?')
        if y=='n':
            print('Corrija o código e tente de novo e volte para o começo de tudo')
        elif y=='s':
            print('Parabéns!')
            break
        else:
            pass
    else:
        pass