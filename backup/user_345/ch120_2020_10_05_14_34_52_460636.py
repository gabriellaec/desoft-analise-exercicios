dinheiro = 100
while jogo_valido:
     while dinheiro>0:
         print ('Você tem {0} dinheiros'. format (dinheiro))
         aposta=int(input('Qual quantia deseja apostar? ')
         if aposta == 0:
             jogo_valido == False
                   break
         else:
             pass
         como_aposta=input('A aposta será em número (n) ou paridade (p): ')
         if como_aposta == 'n':
             numero=int(input('Numero da aposta entre 1 e 36: ')
             roleta = random.randint(1, 36)
             if numero == roleta:
                dinheiro += 35*aposta
             else:
                dinheiro-=aposta
         if como_aposta == 'p':
             par_impar=input('Aposta em par (p) ou impar (i): ')
             roleta = random.randint(1, 36)
             if roleta % 2 ==0 and par_impar == 'p':
                dinheiro += aposta
             elif roleta %2 != 0 and par_impar == 'i':
                dinheiro += aposta
             else:
                dinheiro -= aposta
        