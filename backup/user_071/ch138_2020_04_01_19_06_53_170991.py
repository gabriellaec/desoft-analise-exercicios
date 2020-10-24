def fluxograma():
    f1=input("o programa está funcionando? (s/n)")
    if f1=='n':
        return('Corrija o código e tente de novo')
        print (f1)
    if f1 =='s':
        f2=input('o codigo produz o resultado correto?(s/n)')
        if f2 =='n':
            return('Corrija o código e tente de novo')
            print (f2)
        if f2 == 's':
            return ('Parabéns!')