import random as rdm
j = True
d = 100
while d > 0 and j:
    print('Você possui {0} dinheiros'.format(d))
    a = float(input('Aposte um valor: '))

    if a == 0:
        j = False

    elif a != 0:
        x = input('A aposta é em um número ou paridade? ')
        r = rdm.randint(1,36)
        print(r)  #Resposta (apagar depois)
        if x == 'n':
            n = int(input('Digite um número de 1 a 36: '))
            if n == r:
                d = d + 35*a
            else: 
                d = d - a
        elif x == 'p':
            pi = input('Escolha: Par ou ímpar: ')
            if pi == 'p':
                if r % 2 == 0:
                    d = d + a
                else:
                    d = d - a
            elif pi == 'i':
                if r% 2 != 0:
                    d = d + a
                else:
                    d = d - a
                
print('Perdedor!')        
        