import random

d1=random.randint(1,6)
d2=random.randint(1,6)
d3=random.randint(1,6)
d=d1+d2+d3

m=10

while m > 0:
    print(m)
    dica = input("Você quer uma dica? ")
    if dica == "sim":
        m=m-1
        n1 = int(input("Digite seu chute. "))
        n2 = int(input("Digite seu chute. "))
        n3 = int(input("Digite seu chute. "))
        if n1==d or n2==d or n3==d:
            print("Está entre os 3")
        else:
            print("Não está entre os 3")
    print(m)
    if m <= 0:
        print("Você perdeu!")
        break
    c = int(input("Digite sua resposta. "))
    if c == d:
        m=m+m*5
        print("Você ganhou com {0} dinheiros!".format(m))
        break
    else:
        m=m-1
    if m <= 0:
        print("Você perdeu!")