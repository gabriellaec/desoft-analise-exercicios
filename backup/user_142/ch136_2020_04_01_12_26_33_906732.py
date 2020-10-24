import random
Dado1 = random.randint(1,6)
Dado2 = random.randint(1,6)
Dado3 = random.randint(1,6)
SomaD = Dado1 + Dado2 + Dado3

credito = 10

Dica = input('Quer uma dica?')

Creditos = int(input('Você tem {} créditos'. format(credito)))
               if Creditos == '0':
               print('Você perdeu')
               else:
               print('Quer uma dica?')
                   if Dica =='sim':
                    credito = credito - 1
                    Perg1 = int(input('Qual o primeiro numero?')
                    Perg2 = int(input('Qual o segundo numero?')
                    Perg3 = int(input('Qual o terceiro numero?')   
                    SomaP = Perg1 + Perg2 + Perg3
                        if SomaD == Perg1 or SomaD == Perg2 or SomaD == Perg3
                                print('Está entre os 3')
                        else:
                                print('Não está entre os 3')
                                