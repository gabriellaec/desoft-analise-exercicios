import random
c = 100
game_on = True
while game_on:
    if c > 0:
        a = random.randint(0,36)
        print(c)
        v = int(input('Qual será o valor apostado? '))
        if 0<v<=c:
            paridade = input('A aposta é um número ou uma paridade? ')
            if paridade == 'n':
                x = int(input('Qual o número? '))
                if x == a:
                    c = c + (v*35)
                else:
                    c = c - v
            elif paridade == 'p':
                g = input('A aposta será em par ou ímpar? ')
                if g == 'p':
                    if a%2 == 0:
                        c = c + v
                    else:
                        c = c - v
                elif g == 'i':
                    if a%2 == 0:
                        c = c - v
                    else:
                        c = c + v
        else:
            print('FIM')
            break
        
    else:
        print('FIM')
        break