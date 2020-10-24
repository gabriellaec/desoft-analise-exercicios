from random import randint
d = 10
valor1 = randint (1,6)
valor2 = randint (1,6)
valor3 = randint (1,6)
soma = valor1 + valor2 +valor3

k = input ("Você quer uma dica?")
while k == "sim":
    p = int (input("Escolha um número: "))
    m = int (input("Escolha um número: "))
    n = int (input("Escolha um número: "))
    d-=1
    print (d)
    if soma == p or soma == m or soma == n:
        print ("Está entre os 3")
    else:
        print ("Não está entre os 3")
while k == "não" and d > 0:
    print (d)
    chute = int (input("Qual é a soma?"))
    if chute == soma:
        d += 5 * d
        print ("Você ganhou o jogo com", d, "dinheiros!")
    else:
         d-=1
print ("Você perdeu!")