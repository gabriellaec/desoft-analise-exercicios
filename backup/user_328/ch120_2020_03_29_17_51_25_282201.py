import random 
din=100
valor=1
while din != 0 and valor !=0:
    print('Você tem {0} reais'.format(din))
    valor= int(input('Digite um valor: '))
    if valor != 0 :
        aposta= input('Esta aposta é um número(n) ou uma paridade(p)?: ')
        sorteio= random.randint(0,36)
        if aposta == 'n':
            numero = int(input('Digite um número de 1 a 36: '))
            if numero == sorteio:
                din = din + valor*35
                print(din)
            else:
                din = din - valor
                print(din)
        elif aposta == 'p':
            par_impar = input('Digite p para par ou i para ímpar: ')
            if sorteio %2 == 0:
                if par_impar= 'p':
                    din= din + valor
                    print(din)
                elif par_impar == 'i':
                    din = din - valor 
                    print(din)
            elif sorteio %2 != 0:
                if par_impar == 'i':
                    din = din + valor 
                    print(din)
                else:
                    din= din - valor 
                    print(din)
                    
print('Game Over')