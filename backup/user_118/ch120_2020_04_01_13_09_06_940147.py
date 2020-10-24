from random import randint
programa=True

dinheiro=100
print (dinheiro)

while programa:
    tipo=str(input('A aposta é em um número ou em paridade?' ))
    aposta=int(input('Qual valor da aposta? '))
    if aposta<=0:
        programa=False
    if aposta>0:
        if tipo=='n':
            a=int(input('Qual é o número da aposta? '))
            print (a)
            numero=randint(1,36)
            print (numero)
            if a==numero:
                dinheiro+=35*aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
        if tipo=='p':
            numero=randint(0,36)
            print (numero)
            if numero%2==0 or numero==0:
                dinheiro+=aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
        if tipo=='i':
            numero=randint(0,36)
            print (numero)
            if numero%2!=0 or numero!=0:
                dinheiro+=aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
