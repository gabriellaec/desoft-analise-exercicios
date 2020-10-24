import random as rdm

d = 100
while d>0:
    print('Você possui {0} dinheiros'.format(d))
    a = float(input('Aposte um valor'))
    x = input('A aposta é em um número ou paridade?')
    if x = 'n':
        n = input('Digite um número de 1 a 36')
        r = rdm(1,36)
        if n = r:
             d = d + 35*a
        else: d = d - a
    elif x = 'p':
        pi input('Escolha: Par ou ímpar?')
        i = rdm('p','i')
        if pi = i:
            d = d + a
        elif pi != i:
            d = d - a
        
        
    