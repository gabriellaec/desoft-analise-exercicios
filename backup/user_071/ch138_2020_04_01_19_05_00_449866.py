def fluxograma():
    f1=input("o programa está funcionando? (s/n)")
    if f1=='n':
        print('corrija o codigo e tente novamente')
        return f1
    if f1 =='s':
        f2=input('o codigo produz o resultado correto?(s/n)')
        if f2 =='n':
            print('corrija o codigo e tente de novo')
            return f2
        if f2 == 's':
            return ('parabens!')