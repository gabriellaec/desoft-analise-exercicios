import random as rdm

j = True
d = 100
#Esse while abaixo vai rodar em ''loop'' enquanto o dinheiro do jogador for maior que 0 (d > 0), e o ''j'' é pra se, caso o jogador aposte 0 dinheiros, o jogo não rode (note que essa condição está acima das outras)
while d > 0 and j:
print('Você possui {0} dinheiros'.format(d))
a = float(input('Aposte um valor: '))
   if a == 0:
        j = False
#Pergunta pro jogador
   elif a != 0:
        x = input('A aposta é em um número ou paridade? ')
        r = rdm.randint(0,36)
#Se ele escolhe 'n', a aposta é em número, logo satizfaz a condição x==n abaixo
   if x == 'n':
        n = int(input('Digite um número de 1 a 36: '))

        #Se o jogador acerta, a primeira condição é satizfeita, se ele erra, automaticamente vai pro 'else'

        if n == r:

                d = d + 35*a

                print('Acertou!')

            else: 

                d = d - a



        #Abaixo é se o jogador escplhe a aposta para 'par'



        elif x == 'p':

            pi = input('Escolha: Par ou ímpar: ')

            if pi == 'p':



                #Esse r % 2 == 0 significa que, se o resto da divisão r / 2 for igual a zero, a condição é satisfeita

                

                if r % 2 == 0:

                    d = d + a

                    print('Acertou!')

                else:

                    d = d - a

            elif pi == 'i':

                if r% 2 != 0:

                    d = d + a

                    print('Acertou!')

                else:

                    d = d - a

                

print('Perdedor!')  

print('Você possui {0} dinheiros'.format(d))