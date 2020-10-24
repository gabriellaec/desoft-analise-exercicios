from random import randint
programa=True

dinheiro=100

aposta=int(input('Qual valor da aposta? '))

while dinheiro>0:
    if aposta<=0:
        programa=False
    else:
        tipo=str(input(A aposta é em um número ou em paridade?))
        if tipo=='n':
            a=int(input('Qual é o número da aposta? '))
            return a
            numero=randint(1,36)
            print (numero)
            if a==numero:
                dinheiro+=35*aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
        if tipo=='p':
            numero=randint(1,36)
            print (numero)
            if numero%2==0:
                dinheiro+=aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
        if tipo=='i':
            numero=randint(1,36)
            print (numero)
            if numero%2!=0:
                dinheiro+=aposta
                print ('Seu saldo atual é:', + dinheiro)
            else:
                dinheiro-=aposta
                print ('Seu saldo atual é:', + dinheiro)
            


