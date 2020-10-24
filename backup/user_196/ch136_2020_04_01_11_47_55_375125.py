from random import randint
valor1 = randint (1,6)
valor2 = randint (1,6)
valor3 = randint (1,6)
soma = valor1 + valor2 +valor3
d = 10
chute = int (input("Qual é a soma?"))
while d >= 0:
    print(d)
    k = input ("Você quer uma dica?")
    while k == "sim":
        d-=1
        p = int (input("Escolha um número: "))
        m = int (input("Escolha um número: "))
        n = int (input("Escolha um número: "))
        if valor == p or valor == m or valor == n:
                 print ("Está entre os 3")
        else:
                 print ("Não está entre os 3")
     print(d)
     chute = int (input("Qual é a soma?"))
     if chute == valor:
         d += 5 *d
         print ("Você ganhou o jogo com", d, "dinheiros!")
     else:
         d-=1
print ("Você perdeu!")