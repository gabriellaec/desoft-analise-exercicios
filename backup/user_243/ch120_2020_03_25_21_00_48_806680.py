import random
d=100
while d>0:
    e=random.randint(0,36)
    print (f"Dinheiro disponi­vel:{d}")
    a=int(input("Aposte um valor:"))
    if a==0:
        break
    elif a>d:
        print ("você não tem dinehiro suficiente")
    else:
        b=input("tipo de aposta (p-paridade;n-numero):")
        if b=="n":
            c=int(input("Escolha um numero entre 1 e 36:"))
            if c==e:
                d=d+a*35
            else:
                d=d-a
        if b=="p":
            p=input("par ou impar:")
            if e%2==0:
                e="p"
            else:
                e="i"
            if e==p:
                d=d+a
            else:
                d=d-a
