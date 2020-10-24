import random
a=1
total_de_dinheiro=100
while a>0 and total_de_dinheiro>0:
    print('saldo atual:{0}'.format(total_de_dinheiro))
    Aposta=int(input('quanto quer aposta?'))
    if Aposta==0:
        a-=1
        print('saiu')
    elif Aposta<=total_de_dinheiro:
        resultado=random.randint(0,36)
        tipo_de_aposta=input('tipo de aposta n ou p:')
        if tipo_de_aposta=='n':
            x=int(input('escolhe um numero de 0 a 36?'))
            if x==resultado:
                total_de_dinheiro=total_de_dinheiro+Aposta*35
            else:
                total_de_dinheiro=total_de_dinheiro - Aposta
        elif tipo_de_aposta=='p':
            y=input('i ou p?')
            if resultado%2==0:
                v='p'
                if y==v:
                    total_de_dinheiro=total_de_dinheiro+Aposta
                else:
                    total_de_dinheiro=total_de_dinheiro-Aposta
            else:
                v='i'
                if y==v:
                    total_de_dinheiro=total_de_dinheiro+Aposta
                else:
                    total_de_dinheiro=total_de_dinheiro-Aposta
        print(resultado)