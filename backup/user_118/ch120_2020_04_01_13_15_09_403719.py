from random import randint
programa=True

dinheiro=100
print (dinheiro)

while programa:
    aposta=float(input('Qual valor da aposta? '))
    if aposta<=0 or dinheiro<=0:
        programa=False
    if aposta>0:
        tipo=str(input('A aposta é em um número ou em paridade?' ))
        if tipo=='n':
            a=float(input('Qual é o número da aposta? '))
            print (a)
            numero=randint(0,36)
            print (numero)
            if a==numero:
                dinheiro+=35*aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
                if aposta<=0 or dinheiro<=0:
                    programa=False
        if tipo=='p':
            numero=randint(0,36)
            print (numero)
            if numero%2==0 or numero==0:
                dinheiro+=aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
                if aposta<=0 or dinheiro<=0:
                    programa=False
        if tipo=='i':
            numero=randint(0,36)
            print (numero)
            if numero%2!=0 or numero!=0:
                dinheiro+=aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
                if aposta<=0 or dinheiro<=0:
                    programa=False
