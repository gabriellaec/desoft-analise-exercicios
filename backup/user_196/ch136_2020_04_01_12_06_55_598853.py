from random import randint
d = 10
while d > 0:
    print(d)
    valor1 = randint (1,6)
    valor2 = randint (1,6)
    valor3 = randint (1,6)
    soma = valor1 + valor2 +valor3
    
    k = input ("Você quer uma dica?")
    while k == "sim":
        d-=1
        p = int (input("Escolha um número: "))
        m = int (input("Escolha um número: "))
        n = int (input("Escolha um número: "))
        if soma == p or soma == m or soma == n:
                 print ("Está entre os 3")
        else:
                 print ("Não está entre os 3")
    print(d)
    chute = int (input("Qual é a soma?"))
    if chute == soma:
        d += 5 * d
        print ("Você ganhou o jogo com", d, "dinheiros!")
    else:
         d-=1
print ("Você perdeu!")