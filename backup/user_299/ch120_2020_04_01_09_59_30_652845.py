import math
from random import randint

dinheiros = 100
while dinheiros>0:
 print("Você tem {0} dinheiros disponiveis".format(dinheiros))
 aposta=int(input("Digite o valor de sua aposta:"))
 while aposta>dinheiros or aposta==0:
 print("Você deve apostar um valor menor ou igual a {0} e maior qu
e zero".format(dinheiros))
 aposta=int(input("Digite novamente o valor de sua aposta:"))
 modalidade=input("Se você deseja apostar em Número digite 'n', mas se
deseja apostar em Paridade digite 'p':")
 if modalidade == 'n':
 numero_escolhido = int(input("Em qual número inteiro deseja aloca
r suas apostas? "))
 numero_sorteado = randint(1,36)
 if numero_escolhido == numero_sorteado:
 dinheiros=dinheiros+35*aposta
 print("O número sorteado foi o {0}, logo você acertou o nùmer
o e agora você tem {1} dinheiros".format(numero_sorteado,dinheiros))
 else:
 dinheiros=dinheiros-aposta
 print("O número sorteado foi o {0}, logo você errou o nùmero
e agora você tem {1} dinheiros".format(numero_sorteado,dinheiros))
 elif modalidade == 'p':
 paridade = input("Se você deseja apostar em em um número par digi
te 'p' ,mas se você deseja apostar em um numero ímpar digite 'i':")
 numero_sorteado = randint(1,36)
 if paridade == 'p' and numero_sorteado%2 == 0:
 dinheiros=dinheiros+aposta
 print("O número sorteado foi o {0}, logo você acertou o nùmer
o e agora você tem {1} dinheiros".format(numero_sorteado,dinheiros))
 elif paridade == 'p' and numero_sorteado%2 != 0:
 dinheiros=dinheiros-aposta
 print("O número sorteado foi o {0}, logo você errou o nùmero
e agora você tem {1} dinheiros".format(numero_sorteado,dinheiros))
 elif paridade == 'i' and numero_sorteado%2 != 0:
 dinheiros=dinheiros+aposta
 print("O número sorteado foi o {0}, logo você acertou o nùmer
o e agora você tem {1} dinheiros".format(numero_sorteado,dinheiros))
 else:
 dinheiros=dinheiros-aposta
 print("O número sorteado foi o {0}, logo você errou o nùmero
e agora você tem {1} dinheiros".format(numero_sorteado,dinheiros))