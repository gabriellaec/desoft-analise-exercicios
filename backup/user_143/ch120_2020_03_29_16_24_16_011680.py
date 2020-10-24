import random
saldo=100
while saldo!=0:
      print('Você tem {0} dinheiros'. format(saldo))
      valor=False
      while not valor:
            va=int(input('Aposte um valor:'))
            if va == 0:
                  valor=True
                  saldo-=saldo
                  print('o jogo acabou! seu saldo agora é {0}'. format(saldo))
            elif va <= saldo and va>0:
                  valor=True
            else:
                  print('digite outra aposta:')
      if saldo>0:
            tipo=input('Que tipo de aposta você deseja:')
            if tipo == 'n':
                  b=int(input('qual numero você aposta:'))
                  num=random.randint(0, 36)
                  print(num)
                  if num == b:
                        print('Parabéns! você ganhou {0} dinheiros'. format(va*35))
                        saldo+=va*35
                  else:
                        print('Que pena, você perdeu {0} dinheiros'. format(va))
                        saldo-=va
            if tipo == 'p':
                  p_i=input('escolha entre p ou i:')
                  num2=random.randint(0,36)
                  print(num2)
                  if num2%2==0 and p_i == 'p':
                        print('parabéns, você ganhou {0} dinheiros'. format(va))
                        saldo+=va
                  elif num2%2!=0 and p_i == 'p':
                        print('Que pena, você perdeu {0} dinheiros'. format(va))
                        saldo-=va
                  elif num2%2==0 and p_i == 'i':
                        print('Que pena, você perdeu {0} dinheiros'. format(va))
                        saldo-=va
                  else:
                        print('parabéns, você ganhou {0} dinheiros'. format(va))
                        saldo+=va
          