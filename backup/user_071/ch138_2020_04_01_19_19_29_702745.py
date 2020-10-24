def fluxograma():
    i=True
    while i==True :
        f1=input("o programa está funcionando? (s/n)")
        while f1=='n':
            print('Corrija o código e tente de novo')
            f1=input("o programa está funcionando? (s/n)")
        if f1=='s':
            f2=input('o codigo produz o resultado correto?(s/n)')
            if f2=='s':
                i=False
                print('Parabéns')
            if f2=='n':
                print('Corrija o código e tente de novo')
                f1=='n'