from random import randint
dinheiro=100
while dinheiro>0:
    bet=int(input('quanto deseja apostar?: '))
    dinheiro=dinheiro-bet
    if bet!=0:
        paridade=input('par ou impar?(digite n ou p): ')
        if paridade=='n':
            x=int(input('escokha uma numero de 1 a 36: ')) 
            y=randint(0, 36)
            print (y)
            if x==y:
                dinheiro=dinheiro+(35*bet)
                print (dinheiro)
            else:
                dinheir-=bet
                print (dinheiro)
        elif paridade=='p':
            z=input('par ou impar?: ')
            y=randint(0, 36)
            if y%2==0 and z=='p':
                dinheiro+=bet
                print (dinheiro)
            elif y%2!=0 and z=='i':
                dinheiro+=bet
                print (dinheiro)
            else:
                dinheiro-=bet
                print (dinheiro)