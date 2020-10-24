import random as rd
dinheiro=100
while dinheiro >0:
    numero=rd.randint(1, 36)
    if dinheiro == 0:
        break
    print ('voce tem', dinheiro, 'dinheiro')
    valor=int(input('qunato quer apostar? '))
    if valor == 0:
        break
    aposta=input('quer apostar em um numero ou em uma paridade? ')
    if aposta == 'n':
        casa=int(input('escolha um numero de 1 a 36: '))
        if casa == numero:
            dinheiro+=valor*35
        else:
            dinheiro-=valor
    if aposta == 'p':
        paridade=input('par ou impar: ')
        if paridade == 'p':
            if numero % 2 == 0:
                dinheiro += valor
            else:
                dinheiro-=valor
        else:
            if numero % 2 != 0:
                dinheiro+=valor
            else:
                dinheiro-=valor
if dinheiro == 0:
    print ('acabou seu dinheiro')
else:
    print ('Muito bem voce terminou com', dinheiro, 'dinheiro')