import random
total_de_dinheiro=100
numero_de_apostas=1
while numero_de_apostas>0 and total_de_dinheiro>0:
    resultado=random.randint(0,36)
    Aposta=float(input('quanto quer aposta?'))
    numero_de_apostas+=1
    tipo_de_aposta=input('tipo de aposta n ou p:')
    if tipo_de_aposta=='n':
        x=int(input('escolhe um numero de 0 a 36?'))
        if x==resultado:
            total_de_dinheiro=total_de_dinheiro+Aposta*35
        else:
            total_de_dinheiro=total_de_dinheiro-Aposta
    elif tipo_de_aposta=='p':
        y=input('impar ou par? ')
        if resultado%2==0:
            if 'y'==resultado:
                total_de_dinheiro=total_de_dinheiro+Aposta
            elif 'y'!=resultado:
                total_de_dinheiro=total_de_dinheiro-Aposta
        else:
            if 'y'==resultado:
                total_de_dinheiro=total_de_dinheiro+Aposta
            elif 'y'!=resultado:
                total_de_dinheiro=total_de_dinheiro-Aposta               
    print(total_de_dinheiro)
    print(resultado)