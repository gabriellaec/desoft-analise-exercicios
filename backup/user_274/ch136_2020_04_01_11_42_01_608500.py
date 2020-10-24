import random

d1=random.randint(1,6)
d2=random.randint(1,6)
d3=random.randint(1,6)
d=d1+d2+d3

m=10

print(m)
dica = input("Você quer uma dica? ")
while dica == "sim" and m > 0:
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
    else:
        dica = input("Você quer uma dica? ")

print(m)
if m <= 0:
    print("Você perdeu!")

while m>0:
    c = input("Digite sua resposta. ")
    c=int(c)
    if c == d:
        m=m+m*5
        print("Você ganhou com {0} dinheiros!".format(m))
        break
    else:
        m=m-1
    print(m)
    if m <= 0:
        print("Você perdeu!")