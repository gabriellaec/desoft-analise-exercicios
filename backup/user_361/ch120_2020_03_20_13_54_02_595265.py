from random import randint

dinheiros = 100

while dinheiros > 0:
    print(dinheiros)
    aposta = int(input("Quantos dinheiros quer apostar? "))
    if(aposta == 0):
        break
    else:
        dinheiros -= aposta
    np = input("num ou par (n/p)? ")
    n = randint(0,36)
    if(np == "n"):
        usr = int(input(f"Numero para apostar. Dica, é {n} "))
        if(n == usr):
            dinheiros += aposta*35
         
    if(np == "p"):
        usr = input("Par ou impar (p/i)? ")
        if(n%2 == 0):
            if(usr == "p"):
                dinheiros += aposta