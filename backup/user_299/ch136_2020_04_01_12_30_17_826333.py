from random import radint
dado1 = radint(1,6)
dado2 = radint(1,6)
dado3 = radint(1,6)
somad = dado1+dado2+dado3

dinheiros = 10
print("Você tem {0} dinheiros disponiveis".format(dinheiros)

while dinheiros>0:
    dicas = input('Você deseja alguma dica?(sim ou não)')
    if dicas == 'sim':
      quero_dica=True
      while quero_dica:
          dinheiros = dinheiros - 1
          numero1 = input('Digite um primeiro chute para valor da soma dos dados: ')
          numero2 = input('Digite um segundo chute para valor da soma dos dados: ')
          numero3 = input('Digite um terceiro chute para valor da soma dos dados: ')
          if somad == numero1 or somad == numero2 or somad == numero3:
              print("A soma está entre os 3 valores chutados")
          else:
              print("A soma não está entre os 3 valores chutados")
          print("Você tem {0} dinheiros disponiveis".format(dinheiros)
          vai_querer = input("Você quer mais dicas?")
          if vai_querer = 'sim':
                quero_dica= True
          else:
                quero_dica = False
              

    if dicas == 'não':
        print("Você tem {0} dinheiros disponiveis".format(dinheiros)
        while dinheiros>0:
            chute1 = input('Digite um chute para valor da soma dos dados: ')
            if chute1 == somad:
                dinheiros = dinheiros*6
                print("Você ganhou o jogo com {0} dinheiros".format(dinheiros))
            else: